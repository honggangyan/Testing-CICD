import unittest
from is_prime import is_prime


class Tests(unittest.TestCase):
    """
    Test suite for the is_prime function.
    """

    def test_1(self):
        """Test that 2 is correctly identified as prime."""
        self.assertTrue(is_prime(2))

    def test2(self):
        """Test that 3 is correctly identified as prime."""
        self.assertTrue(is_prime(3))

    def test3(self):
        """
        Test that 25 is correctly identified as non-prime.
        """
        self.assertFalse(is_prime(25))


if __name__ == "__main__":
    unittest.main()
