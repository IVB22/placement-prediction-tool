from flask import Blueprint, request
from ..services.auth_service import AuthService
from ..services.match_service import MatchService
from ..repositories.runs_repo import RunsRepo
from ..utils.pdf_utils import extract_text_from_pdf_bytes

match_bp = Blueprint("match", __name__)

def _auth_user_id():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return None
    token = auth.split(" ", 1)[1].strip()
    uid, err = AuthService.verify_token(token)
    return uid if not err else None

@match_bp.post("/run")
def run_match():
    """
    Accepts multipart/form-data (for PDF) OR JSON.
    Stores request+resume_text+response to Mongo (history).
    Requires JWT.
    """
    user_id = _auth_user_id()
    if not user_id:
        return {"error": "Unauthorized"}, 401

    content_type = (request.content_type or "").lower()

    if "application/json" in content_type:
        data = request.get_json(force=True) or {}
        profile = data.get("profile", {}) or {}
        resume_text = data.get("resume_text", "") or ""
        company = (data.get("company") or "").strip()
        role = (data.get("role") or "").strip()
    else:
        # multipart
        profile = request.form.get("profile_json", "{}")
        try:
            import json
            profile = json.loads(profile)
        except Exception:
            profile = {}

        company = (request.form.get("company") or "").strip()
        role = (request.form.get("role") or "").strip()
        resume_text = (request.form.get("resume_text") or "").strip()

        if "resume_pdf" in request.files and request.files["resume_pdf"].filename:
            pdf_bytes = request.files["resume_pdf"].read()
            pdf_text = extract_text_from_pdf_bytes(pdf_bytes)
            if pdf_text:
                resume_text = (resume_text + "\n" + pdf_text).strip()

    response = MatchService.match(profile, resume_text, company, role)

    # store full resume text + response (history requirement)
    request_doc = {"profile": profile, "resume_text": resume_text, "company": company, "role": role}
    RunsRepo.insert_run(user_id, request_doc, response)

    return response
