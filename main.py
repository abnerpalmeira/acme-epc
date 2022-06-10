from rate import Rate
from employee import Employee
from utility import (
    FileHandler,
    InputHandler,
    ValidationError,
    JSON_FILE_PATH,
    INPUT_FILE_PATH,
)


if __name__ == "__main__":
    try:
        data = FileHandler.open_file(JSON_FILE_PATH)
        input = FileHandler.open_file(INPUT_FILE_PATH)
        employees = []
        rate = Rate(data["rates"])
        InputHandler.process_input(input, employees, data["regex"])
        for e in employees:
            amount = e.calculate_payment(rate)
            print("The amount to pay {0} is: {1:.2f} USD".format(e.name, amount))
    except FileNotFoundError as error:
        print(f"Couldn't find {error.filename}.")
    except ValidationError as error:
        print(error.args[0])
