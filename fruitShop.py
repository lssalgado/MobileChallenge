#!/usr/bin/python
# -*- coding: utf8 -*-

import threading
import os
import requests
import json
import time
from ctypes import *

fruitsUrl = "https://raw.githubusercontent.com/muxidev/desafio-android/master/fruits.json"


def prepareC():

    global cExchanger

    cExchanger_lib = cdll.LoadLibrary("main.so")
    cExchanger = cExchanger_lib.valueExchanger
    cExchanger.argtypes = [c_double]
    cExchanger.restype = c_double


def getResponse(*args):
    r = requests.get(fruitsUrl)
    if args:
        return r.json()
    else:
        global tempFruitsJson
        tempFruitsJson = r.json()


def exchangeValue(*args):
    if args:
        tempFruitsJson = args[0]
        prepareC()
    else:
        global tempFruitsJson
    for i in tempFruitsJson["fruits"]:
        value = float(i["price"])
        i[u"preço"] = "%0.2f" % cExchanger(value)
    if args:
        return tempFruitsJson


def getJson(*args):
    
    if args:
        prepareC()

    thread1 = threading.Thread(target=getResponse)
    thread1.start()

    print "Acessando Url .",
    while thread1.isAlive():
        print ".",
        time.sleep(0.1)

    thread2 = threading.Thread(target=exchangeValue)
    thread2.start()

    print "\n\nConvertendo Valores .",
    while thread2.isAlive():
        print ".",
        time.sleep(0.1)

    return tempFruitsJson


def jsonIterator(obj):

    aux = 0

    fruitsArray = []

    for i in obj:

        i[u"preço"] = "%0.2f" % float(i[u"preço"])
        i[u"price"] = "%0.2f" % float(i[u"price"])

        fruitsArray.append(str(aux) + " - " +
                           i["name"].capitalize() + ": $" + str(i["price"]))
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
    print u"\nPressione Enter para recomeçar."
    if raw_input("") == "":
        start()


def start():
    # os.system("cls||clear")

    fruitsJson = getJson()["fruits"]

    print(u"\n\nFrutas disponíveis:\n")
    for i in jsonIterator(fruitsJson):
        print i

    selectedFruit = getInput(len(fruitsJson))

    print buildString(fruitsJson, selectedFruit)

    restart()


def main():
    try:
        prepareC()
    except exception as e:
        raise e
    finally:
        start()


if __name__ == "__main__":
    main()
