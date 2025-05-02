import os

API_ID    = os.environ.get("API_ID", "22467463")
API_HASH  = os.environ.get("API_HASH", "156c0c4ecf6c03b4eb4ea9ac36e465d0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7452916609:AAEqzdgr9Rq623HdUKa8g9IUnjuPp56q5xk") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
