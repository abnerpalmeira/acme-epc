class Employee:

    def __init__(self,input):
        self.name = input.groups()[0]
        self.worked_hours = []
        for entry in input.groups()[1].split(","):
            print(entry)
