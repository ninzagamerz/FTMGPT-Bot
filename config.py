import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "28776072"))
API_HASH = environ.get("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
BOT_TOKEN = environ.get("BOT_TOKEN", "7063596308:AAEoRUgMgDOa9ia4NIgPXjzfzEg8N1C-ad4")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002152815615"))
ADMINS = int(environ.get("ADMINS", "7042535787"))
DB_URI = environ.get("DB_URI", "mongodb+srv://ftm:ftm@ftmbot.z5iox.mongodb.net/?retryWrites=true&w=majority&appName=ftmbot")
DB_NAME = environ.get("DB_NAME", "ftmbot")
OPENAI_API = environ.get("OPENAI_API", "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")
AI = is_enabled((environ.get("AI","True")), False)
