# Search weather API Feature
Author: Tuan Huynh

table: data/city.csv

## TC0001: Verify that weather forecast results are displayed when user inputted only city value

* Search city <city> weather API
* Verify return status code "200"
* Verify city <city> in weather response result
* Verify weather response schema API

## TC0002: Verify that weather forecast results are not displayed when user inputted only country code

* Search city <country> weather API
* Verify return status code "404"
* Verify that weather forecast results are not displayed

## TC0003: Verify that weather forecast results are displayed when user inputted city combine with country code

* Search city <city> and country code <country> weather API
* Verify return status code "200"
* Verify city <city> in weather response result
* Verify country code <country> in weather response result

