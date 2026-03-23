mport unittest
from calculator import multiply_numbers
 
 
class TestMultiplyNumbers(unittest.TestCase):
 
    def test_multiply_two_positive_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
 
    def test_multiply_multiple_numbers(self):
        self.assertEqual(multiply_numbers(1, 2, 3, 4, 5), 120)
 
    def test_multiply_by_zero(self):
        self.assertEqual(multiply_numbers(5, 0, 3), 0)
 
    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply_numbers(-2, -3), 6)
 
    def test_multiply_mixed_sign_numbers(self):
        self.assertEqual(multiply_numbers(-2, 3), -6)
 
    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply_numbers(1.5, 2.0), 3.0)
 
    def test_multiply_no_arguments(self):
        self.assertEqual(multiply_numbers(), 1)
 
    def test_multiply_single_number(self):
        self.assertEqual(multiply_numbers(7), 7)
 
    def test_invalid_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            multiply_numbers(2, "three", 4)
 
 
if __name__ == "__main__":
    unittest.main()
