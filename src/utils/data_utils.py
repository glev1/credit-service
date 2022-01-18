import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

def load_train_data() -> pd.DataFrame:
    """Load Credit Service data from csv file"""
    logger.info('Loading data')
    file = '../../datasets/cs-training.csv'
    df_train = pd.read_csv(file)
    return df_train
