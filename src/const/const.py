from pathlib import Path
import os


class Const:
    # Project Structure
    TEST_ENV = os.getenv("gauge_environment").lower()
    APP_ID = "NGZiZjQ3YmNmOWFjYzY4NzhhNjEwYzllOWNlNDI2Njg="
    PROJECT_ROOT = str(Path(__file__).parent.parent.parent)
    CONFIG_FILE = PROJECT_ROOT + "/config/config.properties"

    # Define environment URL
    if (TEST_ENV == "staging"):
        URL = "https://api-stg.openweathermap.org/data/2.5"
    elif (TEST_ENV == "qa"):
        URL = "https://api-qa.openweathermap.org/data/2.5"
    else:
        URL = "https://api.openweathermap.org/data/2.5"
