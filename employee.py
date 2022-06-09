from locale import currency
from rate import Rate
class Employee:

    def __init__(self,name,worked_minutes):
        self.name = name
        self.__worked_minutes = worked_minutes

    def calculate_payment(self,rates: Rate):
        amount = 0
        for day,start,end in self.__worked_minutes:
            for r in rates.get_by_day(day):
                rate_start_time = r["start_time"]
                rate_end_time = r["end_time"]
                value = r["value"]
                if rate_start_time <= start and end <= rate_end_time:
                    total_minutes = end-start
                    amount += total_minutes//60*value*100
                    amount += 100*(total_minutes%60)/60*value
                    break
                elif start < rate_end_time  and rate_end_time < end:
                    total_minutes = rate_end_time-start
                    start = rate_end_time+1
                    amount += total_minutes//60*value*100
                    amount += 100*(total_minutes%60)/60*value
        return amount/100

