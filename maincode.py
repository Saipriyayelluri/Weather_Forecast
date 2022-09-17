#Importing modules
from format import print_weather
from api import weather_forecast,weather_data,weather_prediction
import os
from format2 import weather
from format3 import product

#Defining an app function
#THIS PART IS DONE BY DEVICHARAN
def app():
    city = input("Enter the city name that you want search: ")#asking the user to enter the input city name
    print()
    try:
        query = 'q=' + city
        w_data = weather_data(query)
        print_weather(w_data, city)
        print()#This print doesnot  do  anything its just for our clarification for different websites we have used
        # query = city
        # w_forecast = weather_forecast(query)
        # weather(w_forecast, city)
        # print()
        query = city
        w_forecast = weather_prediction(query)
        product(w_forecast, city)
        print()
        os.startfile(f"weatherdata.txt")#creating a text file and printing the data in it.
    except:
        print('City name not found...')
        pass



