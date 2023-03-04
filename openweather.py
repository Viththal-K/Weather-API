import requests

api_key = "<Your API key>"
city = input("Enter city name: ")

# get location code
url_city = "https://api.openweathermap.org/data/2.5/weather?"

url_get = url_city + "appid=" + api_key + "&q=" + city.lower()

response = requests.get(url_get)

status_code = response.status_code
def kel_cal_fah(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

if status_code == 200:

    temp = response.json()['main']['temp']
    temp_c, temp_f = kel_cal_fah(temp)
    description = response.json()['weather'][0]['main']
    city = response.json()['name']
    country = response.json()['sys']['country']
    
    print(f"Weather in {city}, {country} is {description} with a temperature of {temp_c:.2f}°C or {temp_f:.2f}°F")

else:
    print("Unable to retrieve data")
