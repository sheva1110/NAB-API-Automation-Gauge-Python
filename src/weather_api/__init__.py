WEATHER_RES_SCHEMA = {
        "coord": {
            "lon": {'type': 'float'},
            "lat": {'type': 'float'}
        },
        "weather": [
            {
                "id": {'type': 'integer'},
                "main": {'type': 'string'},
                "description": {'type': 'string'},
                "icon": {'type': 'string'}
            }
        ],
        "base": {'type': 'string'},
        "main": {
            "temp": {'type': 'float'},
            "feels_like": {'type': 'float'},
            "temp_min": {'type': 'float'},
            "temp_max": {'type': 'float'},
            "pressure": {'type': 'float'},
            "humidity": {'type': 'float'}
        },
        "visibility": {'type': 'float'},
        "wind": {
            "speed": {'type': 'float'},
            "deg": {'type': 'float'}
        },
        "clouds": {
            "all": {'type': 'float'}
        },
        "dt": {'type': 'float'},
        "sys": {
            "type": {'type': 'float'},
            "id": {'type': 'integer'},
            "country": {'type': 'string'},
            "sunrise": {'type': 'float'},
            "sunset": {'type': 'float'}
        },
        "timezone": {'type': 'float'},
        "id": {'type': 'integer'},
        "name": {'type': 'string'},
        "cod": {'type': 'integer'}
    }
