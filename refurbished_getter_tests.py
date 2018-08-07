import unittest
from refurbished_getter import detailer

mockedJson = {"name":"batata","image":"asdasd","price":"10"}

finalString = "batata\nPrice: $asdasd\nPreco: R$35"

class TestDetailer(unittest.TestCase):
    def test_detailer(self):
        self.assertEquals(detailer(mockedJson), finalString)


if __name__ == '__main__':
    unittest.main()