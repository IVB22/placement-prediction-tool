from pymongo import MongoClient

class MongoExt:
    def __init__(self):
        self.client = None
        self.db = None

    def init_app(self, app):
        self.client = MongoClient(app.config["MONGO_URI"])
        self.db = self.client[app.config["MONGO_DB"]]

mongo = MongoExt()
