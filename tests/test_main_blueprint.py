import unittest

from app.main.views import index


class MainTestCase(unittest.TestCase):
    def test_index(self):
        assert index() == "RadhaKrishnaHanuman"
