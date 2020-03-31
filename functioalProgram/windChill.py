#Calculate effective temprature of weather service
import math

#try except block is used to avoid value error
try:
    #Get temprature from user
    temprature=int(input("Enter temprature between 0-50"))
    #check if temprature is between specified range
    if temprature>=0 and temprature<=50:
        #get wind speed from user
        windSpeed=int(input("Enter wind speed between 3-120"))
        #check if wind speed is between specified range
        if windSpeed>3 and windSpeed<120 :
            #Caluclate wind chill
            windChill= 35.74+0.6215*temprature+(0.4275*temprature-35.75)*(math.pow(windSpeed,0.16))

            print("Temprature : ",temprature)
            print("Wind speed : ",windSpeed)
            print("Wind chill : ",windChill)
        else:
            print("Enter windSpeed between 3-120")
    else:
        print("Enter temprature between 0-50")
except ValueError:
    print("Enter correct values ! ")