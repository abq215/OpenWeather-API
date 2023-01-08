# File:     Abdul Basit_FP_10_2_correction.py
# Name:     Abdul Basit
# Course:   DSC-510 Introduction to Programming
# Desc:     This program connects to the OpenWeather.org API to retrieve weather information for a city either
#           by name and country or Postal Code by using the requests module, which will return a JSON string
#           which is parsed for the information and presented to the user.



import requests


def retrieveweatherbyzip(zip_code):
    url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&appid=21d1599d4364cd94aaeb2de7ddf3b644&units=imperial'.format \
        (zip_code)
    try:
        res = requests.get(url)
        response = res.json()
        return response
    except requests.exceptions.RequestException as e:
        print(e)
        return 0


def retrieveweatherbycity(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=21d1599d4364cd94aaeb2de7ddf3b644&units=imperial'.format \
        (city)
    try:
        res = requests.get(url)
        response = res.json()
        return response
    except requests.exceptions.RequestException as e:
        print(e)
        return 0


def parse_weather(response):
    if response['cod'] == '404':
        print(response['message'])
        return 0
    city_name = response['name']
    temp = response['main']['temp']
    high_temp = response['main']['temp_max']
    low_temp = response['main']['temp_min']
    press_temp = response['main']['pressure']
    humid_temp = response['main']['humidity']
    cloud_cover = response['weather'][0]['description']

    print(f"Current Weather Conditions For {city_name}")
    print('Current Temp: {} degrees'.format(temp))
    print('High Temp: {} degrees'.format(high_temp))
    print('Low Temp: {} degrees'.format(low_temp))
    print('Pressure: {} hPa'.format(press_temp))
    print('Humidity: {}%'.format(humid_temp))
    print('Cloud Cover: {} '.format(cloud_cover))


if __name__ == "__main__":
    while True:
        location = int(input(
            "Welcome! Would you like to lookup weather data by US City or zip code? Enter 1 for US City 2 for zip, "
            "or 0 to exit: "))
        if location == 0:
            print("Thanks for stopping by!")
            break
        elif location == 1:
            location = input('Enter City Name:')
            response = retrieveweatherbycity(location)
            parse_weather(response)
        elif location == 2:
            location = int(input('Enter Zip Code:'))
            response = retrieveweatherbyzip(location)
            parse_weather(response)
        else:
            print('not a valid option')
            break


