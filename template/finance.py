import random
import requests
from pprint import pprint


url= "http://finance.yahoo.com/webservice/v1/symbols/YHOO,AAPL/quote?format=json&view=detail"

data=requests.get(url).json()
pprint(data)