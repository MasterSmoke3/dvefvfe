import unittest

class TestCalculations(unittest.TestCase):

    def test_number_4_calculation(self):
        number_1 = 3
        number_2 = number_1 ** 2 + 10 / 5  
        number_3 = number_1 + number_2 % 2 + 1
        number_4 = number_1 // 3 + number_3
        
        self.assertEqual(number_4, 6)

if __name__ == '__main__':
    unittest.main()
