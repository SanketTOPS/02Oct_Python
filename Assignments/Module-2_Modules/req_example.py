import requests

url="https://restcountries.com/v3.1/all"

req=requests.get(url)

data=req.json()

#print(data)

for i in data:
    #print(i['name']["common"])
    print(i["flags"]["png"])
