"""Contain the configurations used in the package."""
import os

from constants import UNSUPPORTED_FILE_HANDLING_VALID_VALUES, MASK_MODE_VALID_VALUES

MAX_DOC_SIZE_PII_CLASSIFICATION = int(os.getenv('MAX_DOC_SIZE_PII_CLASSIFICATION', 1 * 1024 * 1024))  # 1MB
MAX_DOC_SIZE_PII_DETECTION = int(os.getenv('MAX_DOC_SIZE_PII_DETECTION', 5 * 1024))  # 5KB
PII_ENTITY_TYPES = str(os.getenv('PII_ENTITY_TYPES', 'ALL'))
MASK_CHARACTER = str(os.getenv('MASK_CHARACTER', '*'))
MASK_MODE = MASK_MODE_VALID_VALUES[os.getenv('MASK_MODE', MASK_MODE_VALID_VALUES.MASK.name)]
SUBSEGMENT_OVERLAPPING_TOKENS = int(os.getenv('SUBSEGMENT_OVERLAPPING_TOKENS', 20))
DEFAULT_MAX_DOC_SIZE = int(os.getenv('DEFAULT_MAX_DOC_SIZE', 100 * 1024))
CONFIDENCE_THRESHOLD = float(os.getenv('CONFIDENCE_THRESHOLD', 0.5))
MAX_CHARS_OVERLAP = int(os.getenv('MAX_CHARS_OVERLAP', 200))
DEFAULT_LANGUAGE_CODE = str(os.getenv('DEFAULT_LANGUAGE_CODE', 'en'))
REDACTION_API_ONLY = os.getenv('REDACTION_API_ONLY', 'true').lower() == 'true'

UNSUPPORTED_FILE_HANDLING = UNSUPPORTED_FILE_HANDLING_VALID_VALUES[
    os.getenv('UNSUPPORTED_FILE_HANDLING', UNSUPPORTED_FILE_HANDLING_VALID_VALUES.FAIL.name)]

DETECT_PII_ENTITIES_THREAD_COUNT = int(os.getenv('DETECT_PII_ENTITIES_THREAD_COUNT', 5))
CLASSIFY_PII_DOC_THREAD_COUNT = int(os.getenv('CLASSIFY_PII_DOC_THREAD_COUNT', 2))
PUBLISH_CLOUD_WATCH_METRICS = os.getenv('PUBLISH_CLOUD_WATCH_METRICS', 'true').lower() == 'true'
COMPREHEND_ENDPOINT_URL = None if os.getenv('COMPREHEND_ENDPOINT_URL', '') == '' else os.getenv('COMPREHEND_ENDPOINT_URL')

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
