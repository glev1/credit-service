import os
import json

def set_main_path() -> str:
    """Find main path to the project"""

    return os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__))))
