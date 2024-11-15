import unittest
import group

class TestCases(unittest.TestCase):
    def test_group_by_3(self):
        input1 = [1,2,3,4,5,6,7,8,9,10]
        expected = [[1,2,3],[4,5,6],[7,8,9],[10]]
        result = group.groups_of_3(input1)
        self.assertEqual(expected, result)