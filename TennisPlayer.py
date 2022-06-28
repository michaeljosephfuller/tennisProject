from datetime import date

class TennisPlayer:
    def __init__(self,
                 name,
                 birthday,
                 nationality):
        self.__name = name
        self.__birthday = birthday
        self.__nationality = nationality
    
    @property
    def age(self):
        today = date.today()
        thisYearsBirthday = date(today.year, self.__birthday.month, self.__birthday.day)
        return today.year - self.__birthday.year - (thisYearsBirthday > today)
        