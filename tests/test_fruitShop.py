#!/usr/bin/python
# -*- coding: utf8 -*-

import unittest
from fruitShop import buildString, jsonIterator, validateOption, getJson


class TestGetJson(unittest.TestCase):

    def setUp(self):
        self.mockedJson = {u'fruits': [{u'price': 35, u'pre\xe7o': '122.50', u'image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/265px-Red_Apple.jpg', u'name': u'Apple'}, {u'price': 12, u'pre\xe7o': '42.00', u'image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Bananas_white_background_DS.jpg/320px-Bananas_white_background_DS.jpg', u'name': u'Banana'}, {u'price': 45, u'pre\xe7o': '157.50', u'image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Table_grapes_on_white.jpg/320px-Table_grapes_on_white.jpg', u'name': u'Grapes'}, {u'price': 200, u'pre\xe7o': '700.00', u'image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Pineapple_and_cross_section.jpg/286px-Pineapple_and_cross_section.jpg', u'name': u'Pineapple'}, {u'price': 13, u'pre\xe7o': '45.50', u'image': u'http://www.desicomments.com/wp-content/uploads/2017/05/Cherry-Image-600x570.jpg', u'name': u'cherry'}, {u'price': 12.4, u'pre\xe7o': '43.40', u'image': u'http://www.icecreamnation.org/wp-content/uploads/2013/04/Clementine_orange.jpg', u'name': u'clementine'}, {u'price': 9.5, u'pre\xe7o': '33.25', u'image': u'https://www.homenaturalcures.com/wp-content/uploads/olive.jpg', u'name': u'olive'}, {u'price': 8.75, u'pre\xe7o': '30.63', u'image': u'http://cdn2.stylecraze.com/wp-content/uploads/2013/05/tomato-hair-benefits1.jpg', u'name': u'tomato'},{u'price': 11.75, u'pre\xe7o': '41.13', u'image': u'http://farm3.static.flickr.com/2131/2082287810_47339fc93e.jpg', u'name': u'huckleberry'}, {u'price': 2.75, u'pre\xe7o': '9.63', u'image': u'http://media.mercola.com/assets/images/foodfacts/papaya-nutrition-facts.jpg', u'name': u'papaya'}, {u'price': 5.75, u'pre\xe7o': '20.13', u'image': u'https://www.florihana.com/images/stories/virtuemart/product/FLE019%20-%20LIME.jpg', u'name': u'lime'}, {u'price': 4.75, u'pre\xe7o': '16.63', u'image': u'https://www.organicfacts.net/wp-content/uploads/pear.jpg', u'name': u'pear'}]}
        
    def tearDown(self):
        del self.mockedJson

    def test_getJson_success(self):
        fruitsJson = getJson()
        self.assertDictEqual(fruitsJson, self.mockedJson)

    def test_getJson_exception(self):
        try:
            getJson()
        except BaseException as e:
            self.fail(repr(e))

            


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
        self.mockedList = [{"name": "batata", "image": "asdasd", "price": 1.757, u"preço": 6.15},
                           {"name": "Laranja", "image": "asdasd",
                               "price": 2.55, u"preço": 8.93},
                           {"name": "hamburguer", "image": "asdasd",
                               "price": 3.5, u"preço": 12.25},
                           {"name": "Uva", "image": "asdasd",
                               "price": 4, u"preço": 14},
                           {"name": "arroz", "image": "asdasd", "price": 5, u"preço": 17.5}]

        self.finalList = ['0 - Batata: $1.76', '1 - Laranja: $2.55', '2 - Hamburguer: $3.50',
                          '3 - Uva: $4.00', '4 - Arroz: $5.00']
        self.returnedList = jsonIterator(self.mockedList)

        self.wrongList = [{"name": "batata", "image": "asdasd", "price": 1.757}]

    def tearDown(self):
        del self.mockedList
        del self.finalList

    def test_jsonIterator_success(self):

        # Valida o tamanho e conteúdo da lista retornada #

        self.assertEquals(len(self.returnedList), 5)
        self.assertEquals(self.returnedList, self.finalList)

    def test_jsonIterator_typeError(self):

        # Simula um KeyError ao passar uma lista com chaves faltando #

        with self.assertRaises(KeyError):
            jsonIterator(self.wrongList)


class TestValidateOption(unittest.TestCase):
    # Casos onde a opção selecionada é válida #
    def test_validateOption_valid(self):
        self.assertEquals(validateOption(0, 10), False)
        self.assertEquals(validateOption(9, 10), False)
        self.assertEquals(validateOption(0, 1), False)
        self.assertEquals(validateOption(5, 10), False)

    # Casos onde é necessário escolher uma nova opção #
    def test_validateOption_invalid(self):
        self.assertEquals(validateOption(1, 0), True)
        self.assertEquals(validateOption(-1, 5), True)
        self.assertEquals(validateOption(5, 5), True)
        self.assertEquals(validateOption(0, 0), True)
        self.assertEquals(validateOption("a", 5), True)
        self.assertEquals(validateOption("ç", 5), True)
        self.assertEquals(validateOption("", 5), True)


class TestBuildString(unittest.TestCase):
    def setUp(self):
        self.mockedList = [
            {"name": "batata", "image": "asdasd", "price": "0", u"preço": 0},
            {"name": "batata", "image": "asdasd", "price": "1", u"preço": 3.50},
            {"name": "batata", "image": "asdasd", "price": "2.55", u"preço": 8.92},
            {"name": "batata", "image": "asdasd", "price": "10", u"preço": 35},
            {"name": "batata", "image": "asdasd", "price": "10", u"preço": 35}]

        self.wrongJson = [
            {"name": 1, "image": "asdasd", "price": "0", u"preço": 0},
            {"name": "batata", "image": 1, "price": "0", u"preço": 0},
            {"name": "batata", "image": "asdasd", "price": "asdasd", u"preço": 0},
            {"name": "batata", "image": "asdasd", "price": "0", u"preço": "asdasdasd"}]

        self.finalString = u"\n%i - %s\nPrice:  $%s\nPreço: R$%s"

    def tearDown(self):
        del self.mockedList
        del self.wrongJson
        del self.finalString

    # Valida os casos onde é esperado sucesso #
    def test_buildString_success(self):
        i = 0
        while i < len(self.mockedList):
            self.assertEquals(buildString(self.mockedList, i), self.finalString % (
                i, self.mockedList[i]["name"].capitalize(), self.mockedList[i]["price"], self.mockedList[i][u"preço"]))
            i += 1

    # Valida que o método está protegido a erros de tipagem #
    def test_buildString_typeError(self):
        i = 0
        while i < len(self.wrongJson):
            self.assertRaises(TypeError, buildString(self.wrongJson, i))
            i += 1


if __name__ == '__main__':
    unittest.main()
