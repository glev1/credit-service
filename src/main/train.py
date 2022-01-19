import logging
from src.utils.config import get_default


logger = logging.getLogger(__name__)

LEARNING_RATE = get_default('model', 'learning_rate')
MAX_DEPTH = get_default('model', 'max_depth')
N_ESTIMATORS = get_default('model', 'n_estimators')
EVAL_METRIC = get_default('model', 'eval_metric')
