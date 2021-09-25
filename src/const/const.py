from pathlib import Path


class Const:
    # Project Structure
    URL = "https://openweathermap.org/data/2.5"
    APP_ID = "439d4b804bc8187953eb36d2a8c26a02"
    PROJECT_ROOT = str(Path(__file__).parent.parent.parent)
    CONFIG_FILE = PROJECT_ROOT + "/config/config.properties"
    DATA_INPUT_FILE = PROJECT_ROOT + "/data/%s.properties"
