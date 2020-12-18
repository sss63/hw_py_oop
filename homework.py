import datetime as dt

"""
Класс Calculator 
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
            if record.date == dt.date.today():
                summ += record.amount 

        return summ                

    def get_week_stats(self):
        """
        подсчитывает суммарное количество amount в записях за предыдущую неделю
        """
        summ1 = 0
        for record in self.records:
            if dt.date.today() - record.date < dt.timedelta(weeks=1):
                summ1 += record.amount 
        return summ1
    
"""
Класс Record - запись о событии. Трата ли денег, получение ли калорий.
"""
class Record:
    def __init__(self, amount, comment, date=''):
        """
        Конструктор класса получает три параметра и присваивает их в своим аргументам
        """
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        
"""
Класс CaloriesCalculator - класс калькулятора калорий. Наследник класса Calculator
"""
class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)        
        
    def get_calories_remained(self):
        balance = self.limit - self.get_today_stats() 

        if balance > 0:
            return (
                "Сегодня можно съесть что-нибудь ещё, "
                f"но с общей калорийностью не более {balance} кКал"
            )
        else:
            return "Хватит есть!"

"""
Класс CashCalculator - класс калькулятора денег. Наследник класса Calculator
"""
class CashCalculator(Calculator):
    USD_RATE = 73.51
    EURO_RATE = 89.14

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency=''):
        balance = self.limit - self.get_today_stats()

        if currency == 'usd':
            balance /= self.USD_RATE
            currency = 'USD'          
        elif currency == 'eur':
            balance /= self.EURO_RATE
            currency = 'Euro'          
        else:
            currency = 'руб'          
            
        balance = round(balance , 2)    
        if balance > 0:
            return f"На сегодня осталось {balance} {currency}" 
        elif balance == 0:
            return "Денег нет, держись"
        else:
            return f"Денег нет, держись: твой долг - {-balance} {currency}"






 


# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(2500)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе")) 
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="10.12.2020"))
                
print(cash_calculator.get_today_cash_remained())
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
calories_calculator.add_record(Record(amount=1140, comment="Баночка чипсов.", date="10.12.2020"))
                
print(calories_calculator.get_calories_remained())
# должно напечататься
# Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 230 кКал

print(cash_calculator.get_week_stats())
print(calories_calculator.get_week_stats())
print(calories_calculator.get_today_stats())