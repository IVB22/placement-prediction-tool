from bson import ObjectId
from datetime import datetime, timezone
from ..extensions import mongo

class RunsRepo:
    COL = "runs"

    @staticmethod
    def insert_run(user_id: str, request_doc: dict, response_doc: dict):
        doc = {
            "user_id": ObjectId(user_id),
            "created_at": datetime.now(timezone.utc).isoformat(),
            "request": request_doc,
            "response": response_doc,
        }
        return mongo.db[RunsRepo.COL].insert_one(doc).inserted_id

    @staticmethod
    def list_runs(user_id: str, limit: int = 20):
        cur = mongo.db[RunsRepo.COL].find({"user_id": ObjectId(user_id)}).sort("created_at", -1).limit(limit)
        return list(cur)
