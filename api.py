#Importing web scraping library
import requests
#Defining the function and passing a query argument to it.
#openweather map website link and api
#THIS HAS BEEN DONE BY RISHI
def weather_data(query):
    res = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=af8085b321f6c4faf90c2d93c3d4518c&units=metric')
    return res.json()#returning the data into json format file

#goweather website link
def weather_forecast(query):
    url = requests.get(f"https://goweather.herokuapp.com/weather/%7Bquery%7D%22")
    return url.json()

#visualcross website link and api key
def weather_prediction(query):
    link = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'+ query + '?unitGroup=metric&include=days%2Ccurrent%2Chours%2Calerts&key=CBWJ28TDNGTASJ2DZ4TE4RKL3&contentType=json')
    return link.json()