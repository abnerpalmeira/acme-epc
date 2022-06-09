import re

r = re.compile("([a-zA-Z]+)=(([a-zA-Z]+(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]-(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9](,|$))+)")
with open('input.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        x = r.match(line)
        print(x)