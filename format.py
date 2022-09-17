#importing modules to display date and time
#THIS IS PART IS DONE BY RISHI
from datetime import datetime
time = datetime.now().strftime("%H:%M:%S")
date = datetime.now().date()

#Formatting the web data to display in the output and appending it from OPENWEATHERMAP.COM
def print_weather(result, city):
    a = ("{}'s temperature: {}Â°C".format(city, result['main']['temp']))
    b = ("Wind speed: {} m/s".format(result['wind']['speed']))
    c = ("Description: {}".format(result['weather'][0]['description']))
    d = ("Weather: {}".format(result['weather'][0]['main']))
    with open(f"weatherdata.txt", mode="a") as file:
        file.write('\n' + '\n' + "Hey I am Ronald from OPENWEATHER.COM")
        file.write("\n" "Weather report of the day")
        file.write("\n" + f' Date : {date}  \n Time : {time}  \n Location : {city}')
        file.write("\n" + f"{a} \n {b} \n {c} \n {d} '\n'")


