import os

SECRET = os.getenv("QUIZ_SECRET")
TIMEOUT_SECONDS = int(os.getenv("QUIZ_TIMEOUT", "170"))

# Default to headless unless otherwise set
PLAYWRIGHT_HEADLESS = os.getenv("PLAYWRIGHT_HEADLESS", "1") == "1"
