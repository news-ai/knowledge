import time

from middleware import log, config, esclient
from knowledge import entity_extraction

logger = log.setup_custom_logger('knowledge')
