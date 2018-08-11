#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import requests
import json
import math

fruitsUrl = "https://raw.githubusercontent.com/muxidev/desafio-android/master/fruits.json"


def getJson(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print "Erro %s ao acessar %s" (response.status_code, url)


def exchangeValue(number):
    valor = math.ceil(number * 350) / 100
    return valor


def jsonIterator(obj):

    aux = 0

    print(u"Frutas disponíveis:\n")

    for i in obj:
        print str(aux) + " - " + i["name"] + ": $" + str(i["price"])
        i[u"preço"] = "%0.2f" % exchangeValue(i["price"])
        i[u"price"] = "%0.2f" % i[u"price"]
        aux = aux + 1

    return


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
        " - " + str(objs[number]["name"]) + "\nPrice:  $" + \
        str(objs[number]["price"]) + u"\nPreço: R$" + \
        str(objs[number][u"preço"])


def restart():
    if raw_input(u"Pressione Enter para recomecar.") == "":
        main()


def main():

    os.system("cls||clear")

    fruitsJson = getJson(fruitsUrl)["fruits"]
    jsonIterator(fruitsJson)
    selectedFruit = getInput(len(fruitsJson))

    print buildString(fruitsJson, selectedFruit)

    restart()


if __name__ == "__main__":
    main()
