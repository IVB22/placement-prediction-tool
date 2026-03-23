from flask import Blueprint, request
from ..services.auth_service import AuthService
from ..repositories.runs_repo import RunsRepo

history_bp = Blueprint("history", __name__)

def _auth_user_id():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return None
    token = auth.split(" ", 1)[1].strip()
    uid, err = AuthService.verify_token(token)
    return uid if not err else None

@history_bp.get("")
def history():
    user_id = _auth_user_id()
    if not user_id:
        return {"error": "Unauthorized"}, 401

    limit = int(request.args.get("limit", "20"))
    docs = RunsRepo.list_runs(user_id, limit=limit)

    out = []
    for d in docs:
        out.append({
            "id": str(d["_id"]),
            "created_at": d.get("created_at"),
            "request": d.get("request"),
            "response": d.get("response"),
        })
    return {"runs": out}
