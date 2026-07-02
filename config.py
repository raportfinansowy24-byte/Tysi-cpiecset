from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    VIDEO_PROVIDER = os.getenv(
        "VIDEO_PROVIDER",
        "replicate"
    )

    REPLICATE_API_TOKEN = os.getenv(
        "REPLICATE_API_TOKEN"
    )

    OUTPUT_DIR = Path(
        os.getenv("OUTPUT_DIR", "output")
    )

    TEMP_DIR = Path(
        os.getenv("TEMP_DIR", "temp")
    )

    LANGUAGE = os.getenv(
        "LANGUAGE",
        "pl"
    )

    VIDEO_DURATION = int(
        os.getenv("VIDEO_DURATION", "18")
    )

    WIDTH = int(
        os.getenv("VIDEO_WIDTH", "1080")
    )

    HEIGHT = int(
        os.getenv("VIDEO_HEIGHT", "1920")
    )


settings = Settings()

settings.OUTPUT_DIR.mkdir(exist_ok=True)

settings.TEMP_DIR.mkdir(exist_ok=True)
