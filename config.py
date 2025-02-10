import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "28795512"))
API_HASH = os.getenv("API_HASH", "c17e4eb6d994c9892b8a8b6bfea4042a")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7589052839:AAGPMVeZpb63GEG_xXzQEua1q9ewfNzTg50")
