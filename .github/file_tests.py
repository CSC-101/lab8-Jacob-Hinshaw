import unittest
import file

class TestCases(unittest.TestCase):
    def test1_file(self):
        expected =("Line 1: 3.0"
                   "Line 2: 7.0)"
                   "Line 3: 11.0"
                   "Line 4: 15.0"
                   "Line 5: 19.0")
