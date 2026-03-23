from flask import Blueprint
from .auth_routes import auth_bp
from .match_routes import match_bp
from .history_routes import history_bp

api_bp = Blueprint("api", __name__)
api_bp.register_blueprint(auth_bp, url_prefix="/auth")
api_bp.register_blueprint(match_bp, url_prefix="/match")
api_bp.register_blueprint(history_bp, url_prefix="/history")
