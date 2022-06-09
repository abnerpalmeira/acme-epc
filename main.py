import re
from employee import Employee
from rate import Rate
from utility import FileHandler,InputHandler,ValidationError


if __name__ == '__main__':
    try:
        data = FileHandler.open_file("data.json")
        input = FileHandler.open_file("input.txt")
        employees = []
        InputHandler.process_input(input, employees, data["regex"])
        rate = Rate(data["rates"])
    except FileNotFoundError as error:
        print(f"Couldn't find {error.filename}.")
    except ValidationError as error:
        print(error.args[0])