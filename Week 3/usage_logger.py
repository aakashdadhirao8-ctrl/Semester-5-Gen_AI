import os
import json
import time
from datetime import datetime, timezone
from pymongo import MongoClient
from pymongo.errors import PyMongoError


class UsageLogger:

    def __init__(self):
        mongo_uri = os.getenv("MONGODB_URI")
        self.connected = False
        self.client = None
        self.collection = None

        if mongo_uri:
            try:
                self.client = MongoClient(
                    mongo_uri,
                    serverSelectionTimeoutMS=4000,
                    connectTimeoutMS=4000,
                    socketTimeoutMS=5000,
                    retryWrites=True
                )
                self.client.admin.command("ping")
                db = self.client["llm_monitoring"]
                self.collection = db["api_usage"]
                self.connected = True
                print("✅ Connected successfully to MongoDB Atlas!")
            except Exception as err:
                print("\n⚠️ Note: MongoDB Atlas cluster could not be reached directly.")
                print("   (Reason: Campus Wi-Fi firewall blocking port 27017, cluster paused, or IP not whitelisted).")
                print("   👉 Falling back to local logging in 'api_usage_logs.json' so your program runs smoothly.\n")
        else:
            print("MONGODB_URI not found. Logging locally to 'api_usage_logs.json'.")

    def log_call(self, record):
        record["timestamp"] = datetime.now(timezone.utc).isoformat()

        if self.connected and self.collection is not None:
            for attempt in range(3):
                try:
                    self.collection.insert_one(record)
                    print("✅ Usage details saved to MongoDB Atlas.")
                    return True
                except PyMongoError as error:
                    print(f"MongoDB write attempt {attempt + 1} failed: {error}")
                    if attempt < 2:
                        time.sleep(2 ** attempt)

        # Fallback local persistence
        log_file = os.path.join(os.path.dirname(__file__), "api_usage_logs.json")
        try:
            logs = []
            if os.path.exists(log_file):
                with open(log_file, "r", encoding="utf-8") as f:
                    try:
                        logs = json.load(f)
                    except Exception:
                        logs = []
            clean_record = {k: v for k, v in record.items() if k != "_id"}
            logs.append(clean_record)
            with open(log_file, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2)
            print(f"✅ Usage details logged to {os.path.basename(log_file)}")
            return True
        except Exception as file_err:
            print(f"Warning: could not write local log: {file_err}")
            return False

    def close(self):
        if self.client:
            try:
                self.client.close()
            except Exception:
                pass
