#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """represents the unittest"""
    def test_empty_list(self):
        """Test max_integer with an empty list."""
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        """Test max_integer with a list of positive numbers."""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        """Test max_integer with a list of negative numbers."""
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test max_integer with a list of mixed positive and negative numbers."""
        result = max_integer([10, -2, 3, -4, 7])
        self.assertEqual(result, 10)

    def test_single_number(self):
        """Test max_integer with a list containing a single number."""
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_duplicate_numbers(self):
        """Test max_integer with a list containing duplicate numbers."""
        result = max_integer([5, 5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_float_numbers(self):
        """Test max_integer with a list containing float numbers."""
        result = max_integer([3.5, 2.7, 1.9, 4.2])
        self.assertEqual(result, 4.2)

    def test_mixed_numbers_and_floats(self):
        """Test max_integer with a list containing mixed integers and floats."""
        result = max_integer([10, 2.7, -3, 4.2, 7])
        self.assertEqual(result, 10)

    def test_strings(self):
        """Test max_integer with a list containing strings."""
        with self.assertRaises(TypeError):
            max_integer(["hello", "world"])

    def test_mixed_types(self):
        """Test max_integer with a list containing mixed data types."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4.5, True])

    def test_nan_and_inf(self):
        """Test max_integer with a list containing NaN and inf."""
        with self.assertRaises(ValueError):
            max_integer([float('nan'), 2, 3, 4])
        
        with self.assertRaises(OverflowError):
            max_integer([float('inf'), 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
