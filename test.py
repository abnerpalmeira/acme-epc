import unittest
from unittest.mock import MagicMock
from rate import Rate
from employee import Employee
from utility import (
    FileHandler,
    InputHandler,
    ValidationError,
    JSON_FILE_PATH,
)


class TestFileHandler(unittest.TestCase):
    def test_not_found_file(self):
        """
        Check if the expected exception is thrown when file is not found
        """
        self.assertRaises(FileNotFoundError, FileHandler.open_file, "date.json")


class TestInputHandler(unittest.TestCase):
    def test_invalid_input(self):
        """
        Check if the expected exception is thrown when input is not valid
        """
        input = ["RENE=MO10:00-08:00\n"]
        data = FileHandler.open_file(JSON_FILE_PATH)
        self.assertRaises(
            ValidationError, InputHandler.process_input, input, [], data["regex"]
        )

    def test_unformatted_input(self):
        """
        Check if the expected exception is thrown when input is not unformatted
        """
        input = ["RENE=EU07:00-08:00\n"]
        data = FileHandler.open_file(JSON_FILE_PATH)
        self.assertRaises(
            ValidationError, InputHandler.process_input, input, [], data["regex"]
        )


class TestEmployee(unittest.TestCase):
    def test_calculate_payment(self):
        """
        Check if calculate_payment is calling every method its need to and is returning a expected value
        """
        employees = []
        input = ["RENE=TU07:00-08:00\n"]
        data = FileHandler.open_file(JSON_FILE_PATH)
        rate = Rate(data["rates"])
        rate.get_by_day = MagicMock(
            return_value=[
                {"start_time": 1, "end_time": 540, "value": 20, "currency": "USD"}
            ]
        )
        InputHandler.process_input(input, employees, data["regex"])
        self.assertEqual(employees[0].calculate_payment(rate), 20)
        rate.get_by_day.assert_called_once()


if __name__ == "__main__":
    unittest.main()
