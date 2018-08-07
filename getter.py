#coding: utf-8

import urllib, json
url = "https://raw.githubusercontent.com/muxidev/desafio-android/master/fruits.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
# print data

aux = 0
dolarToReal = 3.5

print len(data["fruits"])

print("Selecione a fruta desejada:")

for i in data["fruits"]:
    print str(aux) + " - " + i["name"] + ": " + str(i["price"])
    aux = aux + 1

fruit = input("")

selectedFruit = data["fruits"][fruit]

print selectedFruit["name"] + "\nPrice:  $" + str(selectedFruit["price"]) + "\nPreco: R$" + str(selectedFruit["price"]*3.5)