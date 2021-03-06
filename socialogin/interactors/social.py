import os
import json
from dataclasses import dataclass
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.join(BASE_DIR, '../')
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, 'social')
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, '.config.json')
config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())


@dataclass
class FaceBook:
  facebook_api_id: str = config_secret['FACEBOOK_API_ID']
  facebook_api_secret: str = config_secret['FACEBOOK_API_SECRET']
  facebook_api_redirect_uri: str = config_secret['FACEBOOK_API_REDIRECT_URI']


@dataclass
class Kakao:
  kakao_api_id: str = config_secret['KAKAO_API_ID']
  kakao_api_redirect_uri: str = config_secret['KAKAO_API_REDIRECT_URI']