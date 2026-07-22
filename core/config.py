from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8080))

HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
