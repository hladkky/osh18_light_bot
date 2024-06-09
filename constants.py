import os

import dotenv


dotenv.load_dotenv("./.env")


MACHINE_ID = os.environ.get("MACHINE_ID")
TARGET = os.environ.get("TARGET")
HUB_ID = os.environ.get("HUB_ID")
SOCKET_ID = os.environ.get("SOCKET_ID")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TARGET_CHAT_ID = os.environ.get("TARGET_CHAT_ID")
CREDENTIALS_EMAIL = os.environ.get("CREDENTIALS_EMAIL")
CREDENTIALS_PASSWORD = os.environ.get("CREDENTIALS_PASSWORD")
USER_AGENT = os.environ.get("USER_AGENT")
CLIENT_VERSION = os.environ.get("CLIENT_VERSION")
APPLICATION_LABEL = os.environ.get("APPLICATION_LABEL")
