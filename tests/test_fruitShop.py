#!/usr/bin/python
# -*- coding: utf8 -*-

import unittest
from fruitShop import buildString, jsonIterator


# class TestGetJson(unittest.TestCase):

#     def test_buildString_success(self):
#         i = 0
#         while i < len(self.mockedList):
#             self.assertEquals(buildString(self.mockedList, i), self.finalString % (
#                 i, self.mockedList[i]["name"], self.mockedList[i]["price"], self.mockedList[i][u"preço"]))
#             i += 1

#     def test_buildString_typeError(self):
#         i = 0
#         while i < len(self.wrongJson):
#             self.assertRaises(TypeError, buildString(self.wrongJson, i))
#             i += 1


# class TestExchangeValue(unittest.TestCase):
#     def test_buildString_success(self):
#         i = 0
#         while i < len(mockedList):
#             self.assertEquals(buildString(mockedList, i), finalString % (
#                 i, mockedList[i]["name"], mockedList[i]["price"], mockedList[i][u"preço"]))
#             i += 1

#     def test_buildString_typeError(self):
#         i = 0
#         while i < len(wrongJson):
#             self.assertRaises(TypeError, buildString(wrongJson,i))
#             i += 1


class TestJsonIterator(unittest.TestCase):
    def setUp(self):
        self.mockedList = [{"name": "batata", "image": "asdasd", "price": 1.757},
                           {"name": "Laranja", "image": "asdasd", "price": 2.55},
                           {"name": "hamburguer", "image": "asdasd", "price": 3.5},
                           {"name": "Uva", "image": "asdasd", "price": 4},
                           {"name": "arroz", "image": "asdasd", "price": 5}]

        self.finalList = ['0 - Batata: $1.76', '1 - Laranja: $2.55', '2 - Hamburguer: $3.50',
                          '3 - Uva: $4.00', '4 - Arroz: $5.00']

        self.finalList1 = [{"name": "batata", "image": "asdasd", "price": 1.757, u"preço":6.15},
                          {"name": "Laranja", "image": "asdasd", "price": 2.55, u"preço":8.93},
                          {"name": "hamburguer", "image": "asdasd", "price": 3.5, u"preço":12.25},
                          {"name": "Uva", "image": "asdasd", "price": 4, u"preço":14},
                          {"name": "arroz", "image": "asdasd", "price": 5, u"preço":17.5}]

    def tearDown(self):
        del self.mockedList
        del self.finalList

    def test_jsonIterator_success(self):
        
        returnedList = jsonIterator(self.mockedList)

        self.assertEquals(len(returnedList), 5)
        self.assertEquals(returnedList, self.finalList)
   
    def test_jsonIterator_typeError(self):
        
        self.assertRaises(TypeError, jsonIterator(self.mockedList))
        


# class TestGetInput(unittest.TestCase):
#     def test_buildString_success(self):
#         i = 0
#         while i < len(mockedList):
#             self.assertEquals(buildString(mockedList, i), finalString % (
#                 i, mockedList[i]["name"], mockedList[i]["price"], mockedList[i][u"preço"]))
#             i += 1

#     def test_buildString_typeError(self):
#         i = 0
#         while i < len(wrongJson):
#             self.assertRaises(TypeError, buildString(wrongJson,i))
#             i += 1


# class TestValidateOption(unittest.TestCase):
#     def test_buildString_success(self):
#         i = 0
#         while i < len(mockedList):
#             self.assertEquals(buildString(mockedList, i), finalString % (
#                 i, mockedList[i]["name"], mockedList[i]["price"], mockedList[i][u"preço"]))
#             i += 1

#     def test_buildString_typeError(self):
#         i = 0
#         while i < len(wrongJson):
#             self.assertRaises(TypeError, buildString(wrongJson,i))
#             i += 1


class TestBuildString(unittest.TestCase):
    def setUp(self):
        self.mockedList = [
            {"name": "batata", "image": "asdasd", "price": "0", u"preço": "0"},
            {"name": "batata", "image": "asdasd", "price": "1", u"preço": "3.50"},
            {"name": "batata", "image": "asdasd", "price": "2.55", u"preço": "8.92"},
            {"name": "batata", "image": "asdasd", "price": "10", u"preço": "35"},
            {"name": "batata", "image": "asdasd", "price": "10", u"preço": "35"}]

        self.wrongJson = [
            {"name": 1, "image": "asdasd", "price": "0", u"preço": "0"},
            {"name": "batata", "image": 1, "price": "0", u"preço": "0"},
            {"name": "batata", "image": "asdasd", "price": 0, u"preço": "0"},
            {"name": "batata", "image": "asdasd", "price": "0", u"preço": 0}]

        self.finalString = u"\n%i - %s\nPrice:  $%s\nPreço: R$%s"

    def tearDown(self):
        del self.mockedList
        del self.wrongJson
        del self.finalString

    def test_buildString_success(self):
        i = 0
        while i < len(self.mockedList):
            self.assertEquals(buildString(self.mockedList, i), self.finalString % (
                i, self.mockedList[i]["name"].capitalize(), self.mockedList[i]["price"], self.mockedList[i][u"preço"]))
            i += 1

    def test_buildString_typeError(self):
        i = 0
        while i < len(self.wrongJson):
            self.assertRaises(TypeError, buildString(self.wrongJson, i))
            i += 1


if __name__ == '__main__':
    unittest.main()
