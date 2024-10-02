import unittest
from unittest.mock import patch
import io

class TestCode(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['10', '10a'])
    def test_input_and_output(self, mock_input, mock_stdout):
        # Исходный код
        """
        Пример кода с ошибкой № 4

        """

        input_int = input("Введите целое число: ")

        if input_int.isdigit():
            print(f'Твое число в степени два равно {int(input_int)**2}')
        else:
            print('Ну я же просил ввести целое число! Ну камон!')


        input_str = input("А теперь напиши еще раз это число и добавь к нему букву: ")  # например, 10а или 24ц

        if input_str.isdigit():
            input_int = int(input_str)
            print(f'{input_int} - это не число')
        else:
            print('Ну я же просил ввести число! Ну камон!')

        # Проверка вывода
        expected_output = "Твое число в степени два равно 100nНу я же просил ввести число! Ну камон!n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
