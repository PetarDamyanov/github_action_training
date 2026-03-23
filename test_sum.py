import unittest
from calculator import sum_numbers
 
 
class TestSumNumbers(unittest.TestCase):
 
    def test_sum_two_positive_numbers(self):
        self.assertEqual(sum_numbers(2, 3), 5)
 
    def test_sum_multiple_numbers(self):
        self.assertEqual(sum_numbers(1, 2, 3, 4, 5), 15)
 
    def test_sum_with_zero(self):
        self.assertEqual(sum_numbers(0, 0, 0), 0)
 
    def test_sum_negative_numbers(self):
        self.assertEqual(sum_numbers(-1, -2, -3), -6)
 
    def test_sum_mixed_sign_numbers(self):
        self.assertEqual(sum_numbers(-5, 10, -3), 2)
 
    def test_sum_floats(self):
        self.assertAlmostEqual(sum_numbers(1.5, 2.5), 4.0)
 
    def test_sum_no_arguments(self):
        self.assertEqual(sum_numbers(), 0)
 
    def test_sum_single_number(self):
        self.assertEqual(sum_numbers(42), 42)
 
    def test_invalid_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            sum_numbers(1, "two", 3)
 
 
if __name__ == "__main__":
    unittest.main()
 
