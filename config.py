import os
from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

class Veez(object):
        admins = {}
        BOT_TOKEN = getenv("BOT_TOKEN", None)
        CHANNEL = int(os.getenv("CHANNEL", "Curhatanmassa"))
        API_ID = int(getenv("API_ID", "7945064"))
        API_HASH = getenv("API_HASH", "9633212b94527280d0cb30f913fe0790")
        SESSION_NAME = getenv("SESSION_NAME", None)
        DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1440"))
        SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
        ASSISTANT_NAME = getenv("ASSISTANT_NAME", "kimasisten")
        BOT_USERNAME = getenv("BOT_USERNAME", "Vcgvideo_bot")
        COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
