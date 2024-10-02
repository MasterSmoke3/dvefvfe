import unittest

def string_manipulation(string):
    """Функция для обработки строки"""
    exclamation_point = '!'
    exclamation_point *= 3
    string = string.strip()
    string = string[:12].upper() if len(string) >= 12 else string.upper()
    return string, exclamation_point

class TestStringManipulation(unittest.TestCase):

    def test_string_transformation(self):
        string, exclamation_point = string_manipulation(' I like administration of hospital   ')
        expected_string = "I LIKE ADMINISTRAT".upper()
        self.assertEqual(string, expected_string)
        self.assertEqual(exclamation_point, "!!!")

    def test_short_string(self):
        string, exclamation_point = string_manipulation('Short string')
        expected_string = "SHORT STRING".upper()
        self.assertEqual(string, expected_string)
        self.assertEqual(exclamation_point, "!!!")

    def test_empty_string(self):
        string, exclamation_point = string_manipulation('')
        expected_string = ''
        self.assertEqual(string, expected_string)
        self.assertEqual(exclamation_point, "!!!")

if __name__ == '__main__':
    unittest.main()
