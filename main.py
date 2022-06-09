import re
from employee import Employee

r = re.compile("^([a-zA-Z]+)=(((MO|WE|FR|T[HU]|S[AU])(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]-(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9](,|$))+)$")
employees = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for idx,line in enumerate(lines):
        match = r.match(line)
        if match:
            name = match.groups()[0]
            worked_hours_string = match.groups()[1]
            employees.append(Employee(name,worked_hours_string))

for e in employees:
    print(e.worked_hours)