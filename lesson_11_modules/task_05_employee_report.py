import random
import datetime
now=datetime.datetime.now()
name=['Kate', 'Alex', 'John', 'Julia', 'Bob']
print('ОТЧЁТ О СОТРУДНИКЕ')
print('Имя:', random.choice(name))
print('Зарплата:', random.randint(30000, 100000))
print ('Дата:',now.strftime('%Y-%m-%d'))
