class Employee:

    def __init__(self,name,worked_hours_string):
        self.name = name
        self.worked_hours_string = worked_hours_string
        self.worked_hours = []
        for entry in worked_hours_string.split(","):
            foo = []
            foo.append(entry[:2])
            foo.append(60*int(entry[2:4])+int(entry[5:7]))
            foo.append(60*int(entry[8:10])+int(entry[11:13]))
            self.worked_hours.append(tuple(foo))
