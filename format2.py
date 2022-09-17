#Importing modules
from datetime import datetime
#Defining the function and formatting the data over in it website GO_WEATHER.COM
#THIS PART IS DONE BY DEVICHARAN
def weather(result, city):
        from datetime import date, timedelta
        time = datetime.now().strftime("%H:%M:%S")
        date1 = datetime.now().date()
        tomorrow = date.today() + timedelta(days=1)
        tomorrow1 = date.today() + timedelta(days=2)
        a = ("Today {}'s Temperature is: {}".format(city, result["temperature"]))
        b = ("Wind speed is: {}".format(result["wind"]))
        c = ("climate condition is: {}".format(result["description"]))
        d = ("---------------------------------------------------------------------")
        e = ("{} temperature is: {}".format(tomorrow, result["forecast"][0]["temperature"]))
        f = ("wind speed is: {}".format(result["forecast"][0]["wind"]))
        g = ("---------------------------------------------------------------------")
        h = ("{} temperature is: {}".format(tomorrow1, result["forecast"][0]["temperature"]))
        i = ("wind speed is: {}".format(result["forecast"][0]["wind"]))
        with open(f"weatherdata.txt", mode="a") as file:
            file.write("\n" + "Hello I am Manish from GO_WEATHER.COM")
            file.write("\n" + f' Date : {date1}  \n Time : {time}  \n Location : {city}')
            file.write("\n" + f"{a} \n {b} \n {c} \n {d} \n {e} \n {f} \n {g} \n {h} \n {i}'\n'")