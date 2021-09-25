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
        URL = "api-stg.openweathermap.org"
    elif (TEST_ENV == "qa"):
        URL = "api-qa.openweathermap.org"
    else:
        URL = "api.openweathermap.org"
