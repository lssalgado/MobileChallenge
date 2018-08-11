#!/usr/bin/python
# -*- coding: utf8 -*-

import unittest
from fruitShop import buildString

mockedJson = [{"name": "batata", "image": "asdasd", "price": "0", u"preço": "0"},
              {"name": "batata", "image": "asdasd", "price": "1", u"preço": "3.50"},
              {"name": "batata", "image": "asdasd", "price": "2.55", u"preço": "8.92"},
              {"name": "batata", "image": "asdasd", "price": "10", u"preço": "35"},
              {"name": "batata", "image": "asdasd", "price": "10", u"preço": "35"}, ]

wrongJson = [{"name": 1, "image": "asdasd", "price": "0", u"preço": "0"},
             {"name": "batata", "image": 1, "price": "0", u"preço": "0"},
             {"name": "batata", "image": "asdasd", "price": 0, u"preço": "0"},
             {"name": "batata", "image": "asdasd", "price": "0", u"preço": 0}]

finalString = u"\n%i - %s\nPrice:  $%s\nPreço: R$%s"


class TestDetailer(unittest.TestCase):
    def test_buildString(self):
        i = 0
        while i < len(mockedJson):
            self.assertEquals(buildString(mockedJson, i), finalString % (
                i, mockedJson[i]["name"], mockedJson[i]["price"], mockedJson[i][u"preço"]))
            i += 1

    def test_buildString_typeError(self):
        i = 0
        while i < len(wrongJson):
            self.assertRaises(TypeError, buildString(wrongJson,i))
            i += 1


if __name__ == '__main__':
    unittest.main()
