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
OPENAI_API = environ.get("OPENAI_API", "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)
AI = is_enabled((environ.get("AI","True")), False)
