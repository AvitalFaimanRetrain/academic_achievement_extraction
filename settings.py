import os
from dotenv import load_dotenv
from retrain_logger.logger import logger_setup

load_dotenv()
logger = logger_setup(__name__)

TAXONOMY_DB = os.environ.get("TAXONOMY_DB", 'DEV_DB')
TAXONOMY_BUCKET = os.environ.get("TAXONOMY_BUCKET")
CLIENT_ID = os.environ.get("STG_RETRAIN_CLIENT_ID")
CLIENT_SECRET = os.environ.get("STG_RETRAIN_CLIENT_SECRET")
ENV = os.environ.get("ENV")
