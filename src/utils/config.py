import os
import json

def set_main_path() -> str:
    """Find main path to the project"""

    return os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__))))

def get_default(config_name: str, parameter: str):
    """Get default configuration values.

    Args:
        config_name (str): Name of the config file.
        parameter (str): Name of the config parameter being loaded.

    Returns:
        The value corresponding to the requested key.

    """
    main_path = set_main_path()
    file = os.path.join(main_path, f"src/conf/{config_name}.json")

    with open(file, encoding='utf-8') as f:
        data = json.load(f)
    return data[parameter]

        
