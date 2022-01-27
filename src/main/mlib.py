"""MLOps Library"""

import json
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import joblib
import logging
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

from src.utils.config import get_default, set_main_path
from src.utils.model_util import get_features
from src.utils.data_utils import load_data

logger = logging.getLogger(__name__)

LEARNING_RATE = get_default('model', 'learning_rate')
MAX_DEPTH = get_default('model', 'max_depth')
N_ESTIMATORS = get_default('model', 'n_estimators')
EVAL_METRIC = get_default('model', 'eval_metric')

RANDOM_STATE = get_default('design','random_state')

STRAT_IMPUTER_NUM = get_default('preprocess','strat_imputer_num')
STRAT_IMPUTER_CAT = get_default('preprocess', 'strat_imputer_cat')

def load_model():
    """Grabs model from disk"""
    dirname = set_main_path()
    filename = os.path.join(dirname, 'src/resources/models/model.joblib')
    clf = joblib.load(filename)
    return clf


def process(X: pd.DataFrame) -> pd.DataFrame:
    """Preprocess data"""

    num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy=STRAT_IMPUTER_NUM)),
    ('std_scaler', StandardScaler())
    ])

    cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy=STRAT_IMPUTER_CAT))
    ])

    num_features, cat_features = get_features()

    full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_features),
    ("cat", cat_pipeline, cat_features)
    ]) 


    X_processed = pd.DataFrame(full_pipeline.fit_transform(X),
                           columns=num_features+cat_features)

    return X_processed

def retrain() -> float:
    """Retrains the model"""

    X, y = load_data(target='SeriousDlqin2yrs')

    X_processed = process(X)

    model = XGBClassifier(learning_rate=LEARNING_RATE,
                         max_depth=MAX_DEPTH,
                         n_estimators=N_ESTIMATORS,
                         use_label_encoder=False,
                        eval_metric=EVAL_METRIC)


    logger.info('Training model')

    model.fit(X_processed, y)

    predict = model.predict_proba(X_processed)
    score = roc_auc_score(y, predict[:,1])

    logger.info(f'Training set accuracy: {score}')

    logger.info('Saving model')
    dirname = set_main_path()
    filename = os.path.join(dirname, 'src/resources/models/model.joblib')
    joblib.dump(model, filename)
    logger.info('Model sucessfully saved')

    return score

def human_readable_payload(predict: float):
    """Takes float and returns back human readable dictionary"""

    readable_prob = str("%.2f" % round(predict*100,2))
    result = {
        "Chance of defaulting": readable_prob,
    }
    return result


def predict(X: dict):
    """Takes features and predicts chance of defaulting"""
    X = [X['rev'], X['debt'], X['inc'], X['age'], X['lowdue'], X['cred'],
    X['highdue'], X['estate'], X['middue'], X['dep']]

    model = load_model()

    num_features, cat_features = get_features()

    X_pred = pd.DataFrame(columns=[*num_features, *cat_features])
    X_pred.loc[0] = X
    
    X_pred_process = process(X_pred)

    predict = model.predict_proba(X_pred_process)[0,1]

    payload = human_readable_payload(predict)

    predict_log_data = {
        "features": X,
        "predict": predict,
        "human_readable_predict": payload
    }
    logging.debug(f"Prediction_log: {predict_log_data}")
    return predict_log_data




