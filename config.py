import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
OWNER_ID = os.environ.get("OWNER_ID", "")