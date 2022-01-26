import pandas as pd
import numpy as np
import logging

from typing import Tuple

logger = logging.getLogger(__name__)

def load_data(target: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Load Credit Service data from csv file"""
    logger.info('Loading data')
    file = 'https://raw.githubusercontent.com/glev1/credit-service/main/datasets/cs-training.csv'
    df = pd.read_csv(file)
    y = df[target]
    X = df.drop(columns=target)
    return X, y

