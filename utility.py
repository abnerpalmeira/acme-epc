import re
import json
from employee import Employee

JSON_FILE_PATH = "data.json"
INPUT_FILE_PATH = "input.txt"


class ValidationError(Exception):
    pass


class FileHandler:
    @staticmethod
    def open_file(path):
        with open(path, "r") as f:
            data = None
            if path[-4:] == "json":
                data = json.load(f)
            else:
                data = lines = f.readlines()
        return data


class InputHandler:
    @staticmethod
    def process_input(input, employees, regex_expression):
        r = re.compile(regex_expression)
        for idx, line in enumerate(input):
            match = r.match(line)
            if match:
                worked_minutes = []
                name = match.groups()[0]
                worked_hours_string = match.groups()[1]
                for entry in worked_hours_string.split(","):
                    foo = []
                    foo.append(entry[:2])
                    foo.append(60 * int(entry[2:4]) + int(entry[5:7]))
                    foo.append(60 * int(entry[8:10]) + int(entry[11:13]))
                    # Check if starting interval is greater than ending
                    if foo[1] > foo[2]:
                        raise ValidationError(
                            f"Invalid input in Line {idx+1} the starting hour is greater than ending hour."
                        )
                    worked_minutes.append(foo)
                employees.append(Employee(name, worked_minutes))
            else:
                raise ValidationError(f"Line {idx+1} of input is invalid.")
