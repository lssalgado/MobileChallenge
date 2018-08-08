#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import urllib
import json


def getContent(str):
    response = urllib.urlopen(str)
    data = json.loads(response.read())
    return data


def selector(obj, aux):

    print(u"Frutas disponíveis:\n")

    for i in obj:
        print str(aux) + " - " + i["name"] + ": $" + str(i["price"])
        aux = aux + 1

    return getInput(aux)


def getInput(aux):
    while True:
        value = raw_input('\nFruta desejada: ')
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


def detailer(obj):
    return obj["name"] + "\nPrice:  $" + \
        str(obj["price"]) + u"\nPreço: R$" + str(obj["price"] * 3.5)


def main():
    os.system('cls||clear')

    url = "https://raw.githubusercontent.com/muxidev/desafio-android/master/fruits.json"
    counter = 0
    dolarToReal = 3.5
    fruit = 0

    fruitsJson = getContent(url)["fruits"]

    fruit = selector(fruitsJson, counter)

    print "\n" + str(fruit) + " - " + detailer(fruitsJson[fruit])


if __name__ == "__main__":
    main()
