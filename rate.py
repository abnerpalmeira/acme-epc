class Rate:

    def __init__(self,rates):
        self.__rates = rates

    def get_by_day(self,day):
        return self.__rates[day]