from bson import ObjectId
from ..extensions import mongo

class UsersRepo:
    COL = "users"

    @staticmethod
    def find_by_email(email: str):
        return mongo.db[UsersRepo.COL].find_one({"email": email.lower().strip()})

    @staticmethod
    def insert_user(user_doc: dict):
        return mongo.db[UsersRepo.COL].insert_one(user_doc).inserted_id

    @staticmethod
    def get_by_id(user_id: str):
        return mongo.db[UsersRepo.COL].find_one({"_id": ObjectId(user_id)})
