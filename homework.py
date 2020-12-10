import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = limit

    def add_record(self, record):
        self.records.append(record)
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
        pass    
    
class Record:
    def __init__(self, amount, comment, date=dt.datetime.today().strftime('%d.%m.%Y')):
        self.amount = amount
        self.comment = comment
        self.date = dt.datetime.strptime(date, '%d.%m.%Y')
        
class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)        
        
    def get_calories_remained():
        pass

# Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более N кКал», если лимит limit не достигнут,
# или «Хватит есть!

class CashCalculator(Calculator):
    USD_RATE = 73.51
    EUR_RATE = 89.14
    

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency='rub'):
        for record in super().records:
            print(record.amount)
            pass 
        pass
        #«На сегодня осталось N руб/USD/Euro» — в случае, если лимит limit не достигнут,
        #или «Денег нет, держись», если лимит достигнут,
        #или «Денег нет, держись: твой долг - N руб/USD/Euro», 






# для CashCalculator 
r1 = Record(amount=145, comment="Безудержный шопинг")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

# для CaloriesCalculator
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")        


print(r1.date)
print(r2.date)


# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе")) 
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained("rub"))
# должно напечататься
# На сегодня осталось 555 руб
