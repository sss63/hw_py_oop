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
        
    def get_calories_remained(self):
        pass

# Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более N кКал», если лимит limit не достигнут,
# или «Хватит есть!

class CashCalculator(Calculator):
    USD_RATE = 73.51
    EUR_RATE = 89.14

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency='rub'):
        summ = 0
        for record in self.records:
            if record.date.date() == dt.datetime.today().date():
                summ += record.amount 

        remain = self.limit - summ 
        
        if currency == 'usd':
            remain /= self.USD_RATE
        elif currency == 'eur':
            remain /= self.EUR_RATE
            
        if remain > 0:
            print(f"На сегодня осталось {remain} {currency}") 
        elif remain == 0:
            print('Денег нет, держись')
        else:
            remain *= -1
            print(f'Денег нет, держись: твой долг - {remain} {currency}')






# для CashCalculator 
r1 = Record(amount=145, comment="Безудержный шопинг")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

# для CaloriesCalculator
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")        


 


# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе")) 
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained("eur"))
# должно напечататься
# На сегодня осталось 555 руб
