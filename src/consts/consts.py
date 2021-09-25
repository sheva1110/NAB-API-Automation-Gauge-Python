from pathlib import Path


class Consts:
    # Project Structure
    URL = "https://ph-api.gobear.com"
    PROJECT_ROOT = str(Path(__file__).parent.parent.parent)
    CONFIG_FILE = PROJECT_ROOT + "/config/config.properties"
    DATA_INPUT_FILE = PROJECT_ROOT + "/data/%s.properties"
