import datetime as dt


class Calculator:
    def __init__(self, limit):
        records = []

    def add_record(self, pl):
        pass

    def get_today_stats(self, parameter_list):
        """
        docstring
        """
        pass

    def get_week_stats(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError    
    


class Record:
    def __init__(self, amount, comment, date=dt.datetime.today()):
        self.amount = amount
        self.comment = comment
        self.date = date



# для CashCalculator 
r1 = Record(amount=145, comment="Безудержный шопинг")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

# для CaloriesCalculator
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")        


print(r2.date)
