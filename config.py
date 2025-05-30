import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7839574004:AAHLKnWsfvRfg42CH3WFbr9t2JS1dmrz8dc") 
    OWNER_ID = os.environ.get("OWNER_ID", "7182427468")