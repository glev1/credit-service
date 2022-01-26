import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import logging
import pandas as pd
from sklearn.compose import ColumnTransformer

from sklearn.impute import SimpleImputer
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from xgboost import XGBClassifier
from src.utils.config import get_default
from src.utils.model_util import save_model
from src.utils.data_utils import load_data

logger = logging.getLogger(__name__)

LEARNING_RATE = get_default('model', 'learning_rate')
MAX_DEPTH = get_default('model', 'max_depth')
N_ESTIMATORS = get_default('model', 'n_estimators')
EVAL_METRIC = get_default('model', 'eval_metric')

RANDOM_STATE = get_default('design','random_state')

STRAT_IMPUTER_NUM = get_default('preprocess','strat_imputer_num')
STRAT_IMPUTER_CAT = get_default('preprocess', 'strat_imputer_cat')

def main():
    X, y = load_data(target='SeriousDlqin2yrs')

    num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy=STRAT_IMPUTER_NUM)),
    ('std_scaler', StandardScaler())
    ])

    cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy=STRAT_IMPUTER_CAT))
    ])

    cat_features = ['age', 'NumberOfTime30-59DaysPastDueNotWorse',
                                     'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
                                     'NumberRealEstateLoansOrLines', 'NumberOfTime60-89DaysPastDueNotWorse',
                                     'NumberOfDependents']

    num_features = ['RevolvingUtilizationOfUnsecuredLines', 'DebtRatio', 'MonthlyIncome']

    full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_features),
    ("cat", cat_pipeline, cat_features)
    ]) 

    X_processed = pd.DataFrame(full_pipeline.fit_transform(X),
                           columns=num_features+cat_features)

    xgb_class = XGBClassifier(learning_rate=LEARNING_RATE,
                         max_depth=MAX_DEPTH,
                         n_estimators=N_ESTIMATORS,
                         use_label_encoder=False,
                        eval_metric=EVAL_METRIC)

    logger.info('Training model')
    xgb_class.fit(X_processed, y)

    predict = xgb_class.predict_proba(X_processed)
    score = roc_auc_score(y, predict[:,1])

    logger.info(f'Training set accuracy: {score}')

    logger.info('Saving model')
    save_model(xgb_class)
    logger.info('Model sucessfully saved')

if __name__ == "__main__":
    main()
    