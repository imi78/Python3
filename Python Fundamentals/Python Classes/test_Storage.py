import unittest

from Storage import Storage


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.storage = Storage(3)

    def test_add_product(self):
        self.assertTrue(self.storage.add_product, [1, 2, 3, 4, 5])
