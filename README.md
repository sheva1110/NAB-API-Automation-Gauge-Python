# OpenWeather-API-Automation-Gauge-Python


## Prerequisites

* Install Python 3.8 or higher.
* Install Gauge on your machine to execute test case.
    *__Gauge__ installed: (windows download file *.msi | MAC: brew install gauge)
    (References: https://docs.gauge.org/getting_started/installing-gauge.html?os=macos&language=python&ide=vscode)
    

## Setup

* Install necessary libraries:
    cd to project path: "/OpenWeather-API-Automation-Gauge-Python"
    ```shell script
    Window: "pip install -r requirements.txt"
    MACOS or Linux: "pip3 install -r requirements.txt"
    ```

Check your GAUGE_PYTHON_COMMAND at env/default/python.properties follow:
   window: python
   MACOS or Linux: python3


## How to run test case:

* Open Terminal, cd to your local directory. Execute command below:

    ```shell script
       gauge run specs -v
    ```


## Project structure:

* Test cases: specs
* Weather API: src/weather_api/api
* Test steps: src/step_impl
* Test data: data/city.csv
* Functions: src/weather_api/api_func.py


## List of API:
    Weather = "/weather"


## View report:
* Open file "reports/html-report/index.html" on Chrome to view result after run test cases. This report is provided by GAUGE FW.


## CI/CD Solution:
* Set up Jenkins server with master and slave.
* Create Jenkins Pipeline and configure with git repository: https://github.com/sheva1110/OpenWeather-API-Automation-Gauge-Python.git
* User docker file to build container from image "python:3.8" and set up libraries.
* User Jenkins file to integrate with docker file to start run automation test.
