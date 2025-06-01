import os
from typing import List

API_ID = os.environ.get("API_ID", "28837889")
API_HASH = os.environ.get("API_HASH", "9d5e9c5b8abcf8b7b930abd259de254e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "7577853954"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002322985853"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "False").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "mongodb+srv://sumitsajwan135:gameno01@cluster0.ja0i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"")
DB_NAME = os.environ.get("DB_NAME", "sumitsajwan135")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1001732273753 -1002322985853").split())) # Add Multiple channel ids
