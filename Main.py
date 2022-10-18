"""weather report  project- reporting ,
location,date,time,temperature,wind speed,description,weather condition
Team 5: Sai priya,Devi charan,Rishi - output form-textfile(notepad)
websites used - OPENWEATHER MAP, GO_WEATHER, VISUALCROSS """

#Importing modules
#THIS PART IS DONE BY SAIPRIYA
from maincode import app
import os
#assinging an empty value to a variable
again = ''
while again != 'n':#iterating the program through  adding a loop and appending previous data to it
    if __name__ == "__main__":
        app()
        print("Do you want to search for more cities ?: ")
        while True:#Iterating to continue for another city or not
            again = input("y-yes/n-no: ")
            if again == "y":
                break
            elif again == "n":
                print("Do you want to create a file of your search list")
                while True: #Asking the user to create a file of searchlist done  by him/her
                    choice = input("y-yes/n-no: ")
                    if choice == "y":
                        os.startfile(f"weatherdata.txt")#Displaying the searchlist file
                        break
                    elif choice == "n":
                        break
                break
            else:
                print("sorry i cant understand")
