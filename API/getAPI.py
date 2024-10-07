import os
from dotenv import load_dotenv


def getAPIKEY():
    load_dotenv()

    return os.getenv("APIKEY")