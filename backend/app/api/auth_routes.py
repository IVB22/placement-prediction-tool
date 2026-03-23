from flask import Blueprint, request
from ..services.auth_service import AuthService
from ..utils.validate import require_fields

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/register")
def register():
    data = request.get_json(force=True) or {}
    missing = require_fields(data, ["name", "email", "password"])
    if missing:
        return {"error": f"Missing fields: {', '.join(missing)}"}, 400

    uid, err = AuthService.register(data["name"], data["email"], data["password"])
    if err:
        return {"error": err}, 400
    return {"ok": True, "user_id": uid}

@auth_bp.post("/login")
def login():
    data = request.get_json(force=True) or {}
    missing = require_fields(data, ["email", "password"])
    if missing:
        return {"error": f"Missing fields: {', '.join(missing)}"}, 400

    payload, err = AuthService.login(data["email"], data["password"])
    if err:
        return {"error": err}, 401
    return payload
