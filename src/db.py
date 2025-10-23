from tinydb import TinyDB
from tinydb.table import Document


class DBHandler:
    def __init__(self, db_path="messages_db.json"):
        self.db = TinyDB(db_path)
        self.messages = self.db.table("messages")

    def store_message(self, json_data):
        message_id = json_data.get("message_id")
        if message_id:
            self.messages.upsert(Document(json_data, doc_id=message_id))
        else:
            self.messages.insert(json_data)

    def get_message(self, message_id):
        return self.messages.get(doc_id=message_id)

    def get_all_messages(self):
        return self.messages.all()

    def delete_message(self, message_id):
        self.messages.remove(doc_ids=[message_id])

    def close(self):
        self.db.close()
