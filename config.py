"""
config.py — All environment variables in one place.
Copy sample.env → .env and fill in your values.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# ── Required ──────────────────────────────────────────────────────────────────
API_ID          = int(os.environ["API_ID"])
API_HASH        = os.environ["API_HASH"]
BOT_TOKEN       = os.environ["BOT_TOKEN"]
STRING_SESSION  = os.environ["STRING_SESSION"]
MONGO_DB_URL    = os.environ["MONGO_DB_URL"]
OWNER_ID        = int(os.environ["OWNER_ID"])

# ── Optional ──────────────────────────────────────────────────────────────────
BOT_NAME         = os.getenv("BOT_NAME", "𝔹𝕠𝕠𝕓𝕠𝕩ᵇʸ ᵉᵛᵈˡᵛ ")
BOT_LINK         = os.getenv("BOT_LINK", "https://t.me/")
UPDATES_CHANNEL  = os.getenv("UPDATES_CHANNEL", "https://t.me/NakaiStore")
SUPPORT_GROUP    = os.getenv("SUPPORT_GROUP", "https://t.me/TestiNakai")
LOGGER_ID        = int(os.getenv("LOGGER_ID", "0"))
PING_IMG_URL     = os.getenv("PING_IMG_URL", "https://ibb.co.com/Gv1bCJs3",)
SESSION_NAME     = os.getenv("SESSION_NAME", "𝔹𝕠𝕠𝕓𝕠𝕩ᵇʸ ᵉᵛᵈˡᵛ ")
PORT             = int(os.getenv("PORT", 10000))

#── Start ───────────────────────────────────────────────────────────────────────
START_ANIMATIONS = [
    "AgACAgUAAxkBAAJEVGospRcWGpLFfyRNX1bSh6yznubOAAICFWsbGgMRVXdh0QABjWWJQwAIAQADAgADeQAHHgQ"
]

# ── Limits ────────────────────────────────────────────────────────────────────
MAX_DURATION_SECONDS = 180000   # 30 minutes
QUEUE_LIMIT          = 2000
COOLDOWN             = 10     # seconds between /play per chat
