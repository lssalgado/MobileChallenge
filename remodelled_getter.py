#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import urllib
import json
import math

fruitsUrl = "https://raw.githubusercontent.com/muxidev/desafio-android/master/fruits.json"


def getJson(url):
    global fruitsJson
    response = urllib.urlopen(url)
    fruitsJson = json.loads(response.read())
    return fruitsJson


def valueExchange(number):
    valor = math.ceil(number * 350) / 100
    return valor


def jsonIterator(obj):

    aux = 0

    print(u"Frutas disponíveis:\n")

    for i in obj:
        print str(aux) + " - " + i["name"] + ": $" + str(i["price"])
        i[u"preço"] = valueExchange(i["price"])
        aux = aux + 1

    return


def validateOption(number):
    while True:
        value = number
        try:
            value = int(value)
        except BaseException:
            print "Opcao invalida, favor selecionar uma fruta:"
            continue
        if value < 0 or value > aux:
            print "Opcao invalida, favor selecionar uma fruta:"

        else:
            break

    return value


def buildString(objs):
    return


def main():
    fruitsJson = getJson(fruitsUrl)["fruits"]
    jsonIterator(fruitsJson)
    validateOption(raw_input(""))
    # print fruitsJson[1][u"preço"]


if __name__ == "__main__":
    main()
