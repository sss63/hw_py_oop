import datetime as dt

"""
Класс 
"""
class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = limit

    def add_record(self, record):
        self.records.append(record)
        
    def get_today_stats(self):
        """
        подсчитывает суммарное количество amount в записях за текущий день
        """
        summ = 0
        for record in self.records:
            if record.date == dt.datetime.today():
                summ += record.amount 

        return self.limit - summ                

    def get_week_stats(self):
        """
        docstring
        """
        summ = 0
        for record in self.records:
            date_week_ago = dt.datetime.today() - dt.timedelta(days=7)
            if record.date.date() > date_week_ago:
                summ += record.amount 
        return summ
    
class Record:
    def __init__(self, amount, comment, date=dt.datetime.today().strftime('%d.%m.%Y')):
        self.amount = amount
        self.comment = comment
        self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        print(type(date), date) 
        print(type(dt.datetime.today()), dt.datetime.today()) 
        print(type(self.date), self.date)

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)        
        
#    def x(self):
#        return super().get_week_stats()

    def get_calories_remained(self):
        balance = super().get_today_stats()

        if balance > 0:
            return (
                "Сегодня можно съесть что-нибудь ещё, "
                f"но с общей калорийностью не более {balance} кКал"
            )
        else:
            return "Хватит есть!"

class CashCalculator(Calculator):
    USD_RATE = 73.51
    EURO_RATE = 89.14

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        balance = super().get_today_stats()
        
        if currency == 'usd':
            balance /= self.USD_RATE
            currency = 'USD'          
        elif currency == 'eur':
            balance /= self.EURO_RATE
            currency = 'Euro'          
        else:
            currency = 'руб.'          
            
        balance = round(balance , 2)    
        if balance > 0:
            return f"На сегодня осталось {balance} {currency}" 
        elif balance == 0:
            return 'Денег нет, держись'
        else:
            balance *= -1
            return f'Денег нет, держись: твой долг - {balance} {currency}'






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
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="11.12.2020"))
                
print(cash_calculator.get_today_cash_remained("usdv"))
# должно напечататься
# На сегодня осталось 555 руб


# создадим калькулятор каллорий с дневным лимитом 1500
calories_calculator = CaloriesCalculator(1500)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
calories_calculator.add_record(Record(amount=1186, comment="Кусок тортика. И ещё один.")) 
# и к этой записи тоже дата должна добавиться автоматически
calories_calculator.add_record(Record(amount=84, comment="Йогурт."))
# а тут пользователь указал дату, сохраняем её
calories_calculator.add_record(Record(amount=1140, comment="Баночка чипсов.", date="12.12.2020"))
                
print(calories_calculator.get_calories_remained())
# должно напечататься
# Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 230 кКал

print(calories_calculator.get_week_stats())
print(cash_calculator.get_week_stats())
