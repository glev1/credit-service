import pandas as pd
import numpy as np
import logging

from typing import Tuple

logger = logging.getLogger(__name__)

def load_data() -> pd.DataFrame:
    """Load Credit Service data from csv file"""
    logger.info('Loading data')
    file = '../../datasets/cs-training.csv'
    df = pd.read_csv(file)
    return df


def stratified_split(data: pd.DataFrame,
                     target: str,
                     n_samples: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Stratified data split.
    Splits data into training and testing dataframes whilst stratifying
    to maintain target variable proportions.
    Args:
        data (DataFrame): Full dataframe including predictors as well as
            target variable.
        target (str): The name of the column containing the target
            variable.
        n_samples (int): The number of samples to include in the test
            set from each target label category.
        Returns:
            tuple: The training and testing dataframes.
    """
    logger.info('Splitting train and test sets')
    n = min(n_samples, data[target].value_counts().min())
    test_df = data.groupby(target).apply(lambda x: x.sample(n))
    test_df.index = test_df.index.droplevel(0)
    train_df = data[~data.index.isin(test_df.index)]
    return train_df, test_df