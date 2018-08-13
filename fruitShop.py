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

    # Carrega a biblioteca C++ para possibilitar as chamadas as suas funções #

    global cExchanger

    cExchanger_lib = cdll.LoadLibrary("main.so")
    cExchanger = cExchanger_lib.valueExchanger
    cExchanger.argtypes = [c_double]
    cExchanger.restype = c_double


def getResponse(*args):

    # Realiza um Get na url e atribui o Json retornado à variável tempFruitsJson #

    r = requests.get(fruitsUrl)
    if args:
        return r.json()
    else:
        global tempFruitsJson
        tempFruitsJson = r.json()


def exchangeValue(*args):

    # Converte os valores de dólar para real e insere a chave 'preço' com seu respectivo valor em cada uma das frutas #

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
    
    # Realiza as chamadas à getResponse e exchangeValue assincronamente e retorna o objeto Json já com os valores convertidos #

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

    # Navega por todos as frutas contidas no objeto passado por parâmetro, alterando seus valores para que fiquem todos com duas casas decimais e retorna os nomes e preços em dólar a serem exibidos no menu principal da aplicação #

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

    # Valida se a opção passada é valida ou não, retornando False quando é válida e True quando não #

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

    # Recebe a opção através do valor digitado no teclado, utiliza validateOption para validar a mesma, retornando a opção apenas quando for uma opção válida #

    selectedFruit = raw_input("\nSelecione a fruta desejada: ")
    while validateOption(selectedFruit, aux):
        selectedFruit = getInput(aux)

    return int(selectedFruit)


def buildString(objs, number):

    # Constrói a string a ser printada a partir do objeto e opção passados por parâmetro #

    return "\n" + str(number) + \
        " - " + str(objs[number]["name"]).capitalize() + "\nPrice:  $" + \
        str(objs[number]["price"]) + u"\nPreço: R$" + \
        str(objs[number][u"preço"])


def restart():

    # Chama a função start para 'recomeçar' a aplicação #

    print u"\nPressione Enter para recomeçar."
    if raw_input("") == "":
        start()


def start():

    # Realiza todas as chamadas para que a aplicação funcione corretamente #

    # os.system("cls||clear")

    fruitsJson = getJson()["fruits"]

    print(u"\n\nFrutas disponíveis:\n")
    for i in jsonIterator(fruitsJson):
        print i

    selectedFruit = getInput(len(fruitsJson))

    print buildString(fruitsJson, selectedFruit)

    restart()


def main():

    # Tenta instânciar a função em C++, caso haja algum erro, dispara uma exceção #

    try:
        prepareC()
    except exception as e:
        raise e
    finally:
        start()


if __name__ == "__main__":
    main()
