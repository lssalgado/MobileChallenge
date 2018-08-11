#!/usr/bin/python
# -*- coding: utf8 -*-

from requests_futures.sessions import FuturesSession
import os
import requests
import json
import math
import time

fruitsUrl = "https://raw.githubusercontent.com/muxidev/desafio-android/master/fruits.json"
session = FuturesSession()

rodando = True

def getResponse(sess, resp):
    global rodando
    rodando = False
    resp.data = resp.json()

def getJson(url):
    future = session.get(fruitsUrl, background_callback=getResponse)
    print "Acessando Url ",
    while rodando == True:
        print ".",
        time.sleep(0.1)
    response = future.result()
    return response.data


def exchangeValue(number):
    valor = math.ceil(number * 350) / 100
    return valor


def jsonIterator(obj):

    aux = 0

    fruitsArray = []

    for i in obj:
        
        i[u"preço"] = "%0.2f" % exchangeValue(i["price"])
        i[u"price"] = "%0.2f" % i[u"price"]

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
    if value < 0 or value > aux:
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

    os.system("cls||clear")

    fruitsJson = getJson(fruitsUrl)["fruits"]


    print(u"Frutas disponíveis:\n")
    for i in jsonIterator(fruitsJson):
        print i

    selectedFruit = getInput(len(fruitsJson))

    print buildString(fruitsJson, selectedFruit)

    restart()


if __name__ == "__main__":
    main()
