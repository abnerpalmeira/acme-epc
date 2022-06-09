import re
from employee import Employee

r = re.compile("^([a-zA-Z]+)=(((MO|WE|FR|T[HU]|S[AU])(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]-(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9](,|$))+)$")
employees = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for idx,line in enumerate(lines):
        match = r.match(line)
        worked_hours = []
        name = ''
        if match:
            name = match.groups()[0]
            worked_hours_string = match.groups()[1]
            for entry in worked_hours_string.split(","):
                foo = []
                foo.append(entry[:2])
                foo.append(60*int(entry[2:4])+int(entry[5:7]))
                foo.append(60*int(entry[8:10])+int(entry[11:13]))
                #Check if starting interval is greater than ending
                if foo[1] > foo[2]:
                    worked_hours = []
                    break;
                worked_hours.append(foo)
        if worked_hours:
            employees.append(Employee(name,worked_hours))
        else:
            print(f"Employee {idx+1} has invalid data.")

for e in employees:
    print(e.worked_hours)