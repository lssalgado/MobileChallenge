#!/usr/bin/python
# -*- coding: utf8 -*-

import threading
import os
import requests
import json
import math
import time
from ctypes import *

fruitsUrl = "https://raw.githubusercontent.com/muxidev/desafio-android/master/fruits.json"

tempFruitsJson = 0

cExchanger_lib = cdll.LoadLibrary("main.so")
cExchanger = cExchanger_lib.valueExchanger
cExchanger.argtypes = [c_double]
cExchanger.restype = c_double

waiting = [True, True]

def getResponse(*obj):
    if obj and waiting:
        tempFruitsJson = obj[0]
        waiting = obj[1]
    else:
        global waiting, tempFruitsJson
    r = requests.get(fruitsUrl)
    waiting[0] = False
    tempFruitsJson = r.json()


def exchangeValue(*obj):
    if obj:
        tempFruitsJson = obj[0]
    else:
        global tempFruitsJson
    for i in tempFruitsJson["fruits"]:
        value = float(i["price"])
        i[u"preço"] = "%0.2f" %  cExchanger(value)
    waiting[1] = False
    

def getJson():
    threading.Thread(target=getResponse).start()
    print "Acessando Url .",
    while waiting[0]:
        print ".",
        time.sleep(0.1)
    threading.Thread(target=exchangeValue).start()
    print "\n\nConvertendo Valores .",
    while waiting[1]:
        print ".",
        time.sleep(0.1)
    return tempFruitsJson
    

def jsonIterator(obj):

    aux = 0

    fruitsArray = []

    for i in obj:
        

        i[u"preço"] = "%0.2f" % float(i[u"preço"])
        i[u"price"] = "%0.2f" % float(i[u"price"])

        fruitsArray.append(str(aux) + " - " + i["name"].capitalize() + ": $" + str(i["price"]))
        aux = aux + 1

    return fruitsArray


def validateOption(number, aux):

    value = number
    try:
        value = int(value)
    except BaseException:
        print u"Opcao inválida."
        return True
    if value < 0 or value > (aux - 1):
        print u"Opcao inválida."
        return True

    else:
        return False


def getInput(aux):
    selectedFruit = raw_input("\nSelecione a fruta desejada: ")
    while validateOption(selectedFruit, aux):
        selectedFruit = getInput(aux)

    return int(selectedFruit)


def buildString(objs, number):
    return "\n" + str(number) + \
        " - " + str(objs[number]["name"]).capitalize() + "\nPrice:  $" + \
        str(objs[number]["price"]) + u"\nPreço: R$" + \
        str(objs[number][u"preço"])


def restart():
    if raw_input(u"Pressione Enter para recomecar.") == "":
        main()


def main():

    # os.system("cls||clear")

    fruitsJson = getJson()["fruits"]


    print(u"\n\nFrutas disponíveis:\n")
    for i in jsonIterator(fruitsJson):
        print i

    selectedFruit = getInput(len(fruitsJson))

    print buildString(fruitsJson, selectedFruit)

    restart()


if __name__ == "__main__":
    main()
