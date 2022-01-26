import os
import logging
import pickle

from xgboost import XGBClassifier

logger = logging.getLogger(__name__)


def set_main_path() -> str:
    """Find main path to the project"""

    return os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__))))


def save_model(model: XGBClassifier) -> None:
    """Save latest trained model to models folder."""

    main_path = set_main_path()
    file = os.path.join(main_path, "src/resources/models/latest_model.pkl")

    with open(file, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(model, outp, pickle.HIGHEST_PROTOCOL)

def load_model() -> XGBClassifier:
    """Load latest trained model from models folder."""
    main_path = set_main_path()
    file = os.path.join(main_path, "src/resources/models/latest_model.pkl")

    with open(file, 'rb') as inp:  # Overwrites any existing file.
        model = pickle.load(inp)

    return model