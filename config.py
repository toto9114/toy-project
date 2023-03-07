from os.path import join, dirname

from dotenv import load_dotenv
from common_lib.utils.env_loader import load_env

dotenv_path = join(dirname(__file__), "./", ".env")
load_dotenv(dotenv_path)

STAGE = load_env("STAGE", "dev")

APP_NAME = load_env("APP_NAME", "food-map-api")

# Logger
LOG_DIR = load_env("LOG_DIRECTORY", "./logs")
LOG_LEVEL = load_env("LOG_LEVEL", "DEBUG")

# EXTERNAL_API
KAKAO_REST_API_KEY = load_env("KAKAO_REST_API_KEY", required=True)
KAKAO_WEB_API_KEY = load_env("KAKAO_WEB_API_KEY", required=True)
