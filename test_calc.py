import unittest
from unittest.mock import patch
import calc

class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
        #return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")
        #return super().tearDownClass()

    def setUp(self):
        print("SetUp")
        self.val1 = 10
        self.val2 = 0
        self.resultAdd = 10

    def tearDown(self):
        print("TearDown")
        pass

    def test_add(self):
        print("test_add")
        result = calc.add(self.val1, self.val2)
        self.assertEqual(result, self.resultAdd)

    def test_substract(self):
        result = calc.substract(self.val1, self.val2)
        self.assertNotEqual(result, 5)

    def test_divide(self):
        # Using context manager
        with self.assertRaises(ValueError):
            calc.divide(self.val1, self.val2)


if __name__ == '__main__':
    unittest.main()