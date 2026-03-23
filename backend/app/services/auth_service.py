import jwt
from datetime import datetime, timedelta, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
from ..repositories.users_repo import UsersRepo

class AuthService:
    @staticmethod
    def register(name: str, email: str, password: str):
        email = email.lower().strip()
        if UsersRepo.find_by_email(email):
            return None, "Email already registered"

        user = {
            "name": name.strip(),
            "email": email,
            "password_hash": generate_password_hash(password),
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        uid = UsersRepo.insert_user(user)
        return str(uid), None

    @staticmethod
    def login(email: str, password: str):
        email = email.lower().strip()
        user = UsersRepo.find_by_email(email)
        if not user or not check_password_hash(user["password_hash"], password):
            return None, "Invalid email or password"

        token = AuthService._issue_jwt(str(user["_id"]), user["email"])
        return {"token": token, "user": {"id": str(user["_id"]), "name": user["name"], "email": user["email"]}}, None

    @staticmethod
    def _issue_jwt(user_id: str, email: str):
        exp = datetime.now(timezone.utc) + timedelta(minutes=current_app.config["JWT_EXPIRES_MIN"])
        payload = {"sub": user_id, "email": email, "exp": exp}
        return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")

    @staticmethod
    def verify_token(token: str):
        try:
            payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            return payload["sub"], None
        except Exception:
            return None, "Invalid or expired token"
