import requests

class Openweather:
    def __init__(self, city):
        self.city = city

        self.api_key = "<API key>"
        
        # get location code
        self.url_city = "https://api.openweathermap.org/data/2.5/weather?"

        self.url_get = self.url_city + "appid=" + self.api_key + "&q=" + self.city.lower()

        self.response = requests.get(self.url_get)

        self.status_code = self.response.status_code
        
    def kel_cal_fah(self, kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit

    def show_open_details(self):
        if self.status_code == 200:

            temp = self.response.json()['main']['temp']
            
            temp_c, temp_f = self.kel_cal_fah(temp)
            
            description = self.response.json()['weather'][0]['main']
            
            city = self.response.json()['name']
            
            country = self.response.json()['sys']['country']
                
            print(f"Weather in {city}, {country} is {description} with a temperature of {temp_c:.2f}°C or {temp_f:.2f}°F")

        else:
            print("Unable to retrieve data")

class Accuweather:
    def __init__(self, city):
        self.city = city
    
        self.api_key = "API key"

        # get location code
        self.url_cityCode = "http://dataservice.accuweather.com/locations/v1/cities/search?"

        self.cityCode_get = self.url_cityCode + "apikey=" + self.api_key + "&q=" + self.city.lower()

        self.response_cc = requests.get(self.cityCode_get)

        self.city_key = self.response_cc.json()[0]['Key']

        self.city = self.response_cc.json()[0]['EnglishName']
        self.country = self.response_cc.json()[0]['Country']['ID']
        
        # get current waether condiditon
        self.url_currentWeather = "http://dataservice.accuweather.com/currentconditions/v1/"

        self.currentWeather_get = self.url_currentWeather + self.city_key + "?apikey=" + self.api_key

        self.response_cw = requests.get(self.currentWeather_get)
    
    def show_acc_details(self):

        self.temp_c = self.response_cw.json()[0]['Temperature']['Metric']['Value']

        self.temp_f = self.response_cw.json()[0]['Temperature']['Imperial']['Value']

        self.description = self.response_cw.json()[0]['WeatherText']
        
        print(f"Weather in {self.city}, {self.country} is {self.description} with a temperature of {self.temp_c:.2f}°C or {self.temp_f:.2f}°F")

        
# creating objects of classes
city_ip = input("Enter city name: ")
obj1 = Openweather(city_ip)
obj2 = Accuweather(city_ip)
print("Output from Openweather API ->")
obj1.show_open_details()
print()
print("Output from Accuweather API ->")
obj2.show_acc_details()
