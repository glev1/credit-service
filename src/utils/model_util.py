import os
import logging
from typing import Tuple

logger = logging.getLogger(__name__)


def get_features() -> Tuple[list, list]:

    num_features = ['RevolvingUtilizationOfUnsecuredLines', 'DebtRatio', 'MonthlyIncome']


    cat_features = ['age', 'NumberOfTime30-59DaysPastDueNotWorse',
                                     'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
                                     'NumberRealEstateLoansOrLines', 'NumberOfTime60-89DaysPastDueNotWorse',
                                     'NumberOfDependents']

    return num_features, cat_features


def set_main_path() -> str:
    """Find main path to the project"""

    return os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__))))

