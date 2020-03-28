import requests
from pprint import pprint
city=input("Enter your city :")
url = "http://api.apixu.com/v1/current.json?key=a65b9295ecc24ae7ba8104243192703&q={}".format(city)

result = requests.get(url)
data = result.json()
#print(result)
pprint(data)
temp = data["current"]["temp_c"]
press=data["current"]["pressure_mb"]
print("Temperature = {} ".format(temp)) 
print("Pressure(Millibars) : {} ".format(press))
