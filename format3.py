#Importing modules
from datetime import timedelta

#Defining the function and formatting the data over init.from VISUALCROSS.COM
#THIS PART IS DONE BY SAIPRIYA
def product(result, city):
    from datetime import datetime
    time = datetime.now().strftime("%H:%M:%S")
    date = datetime.now().date()
    tomorrow = date.today() + timedelta(days=1)
    tomorrow1 = date.today() + timedelta(days=2)
    a = ("Today {}'s Temperature is: {}".format(city, result["days"][0]["tempmax"]))
    b = ("humditylevel is: {}".format(result["days"][0]["humidity"]))
    c = ("windspeed is: {}".format(result["days"][0]["windspeed"]))
    d = ("climatecondition is: {}".format(result["days"][0]["description"]))
    e = ("************************************************************************************")
    f = ("On {}  {}'s Temperature is: {}".format(tomorrow, city, result["days"][1]["tempmax"]))
    g = ("humditylevel is: {}".format(result["days"][1]["humidity"]))
    h = ("windspeed is: {}".format(result["days"][1]["windspeed"]))
    i = ("climatecondition is: {}".format(result["days"][1]["description"]))
    j = ("************************************************************************************")
    k = ("On {}  {}'s Temperature is: {}".format(tomorrow1, city, result["days"][2]["tempmax"]))
    l = ("humditylevel is: {}".format(result["days"][2]["humidity"]))
    m = ("windspeed is: {}".format(result["days"][2]["windspeed"]))
    n = ("climatecondition is: {}".format(result["days"][2]["description"]))
    with open(f"weatherdata.txt", mode="a") as file:  # opening the file  as notepad format
        file.write("\n \n" + "Hello I am William from VISUALCROSS.COM ")
        file.write("\n" "Weather report of the day")
        file.write("\n " + f' Date : {date}  \n Time : {time}  \n Location : {city}')
        file.write(
            "\n" + f"{a} \n {b} \n {c} \n {d} \n {e} \n {f} \n {g} \n {h} \n {i} \n {j} \n {k} \n {l} \n {m} \n {n} ")



