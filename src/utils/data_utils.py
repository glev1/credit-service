import pandas as pd
import numpy as np
import logging

from sklearn.model_selection import train_test_split
from typing import Tuple

logger = logging.getLogger(__name__)

def load_data() -> pd.DataFrame:
    """Load Credit Service data from csv file"""
    logger.info('Loading data')
    file = '../../datasets/cs-training.csv'
    df = pd.read_csv(file)
    return df
