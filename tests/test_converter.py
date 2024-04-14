import unittest
from french_numbers_converter.converter import FrenchNumberConverter

class TestFrenchNumberConverter(unittest.TestCase):
    def setUp(self):
        """Create an instance of the FrenchNumberConverter to use in all tests."""
        self.converter = FrenchNumberConverter()

    def test_convert_21(self):
        """Test the French conversion of the number 21."""
        result = self.converter.convert_to_french(21)
        self.assertEqual(result, "vingt-et-un", "Should be 'vingt-et-un'")

    def test_convert_76(self):
        """Test the French conversion of the number 76."""
        result = self.converter.convert_to_french(76)
        self.assertEqual(result, "soixante-seize", "Should be 'soixante-seize'")

    def test_convert_200000(self):
        """Test the French conversion of the number 76."""
        result = self.converter.convert_to_french(200000)
        self.assertEqual(result, "deux-cent-mille", "Should be 'deux-cent-mille '")

if __name__ == '__main__':
    unittest.main()
