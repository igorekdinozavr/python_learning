try:
    age=int(input('Возраст: '))
    if age<0:
        raise ValueError('Возраст не может быть отрицательным')
except ValueError as error:
    print(error)
else: print(age)
finally: print('Проверка завершена')
