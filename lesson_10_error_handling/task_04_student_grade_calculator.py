students = {
    'Alex': 85,
    'John': 90,
    'Kate': 78,
    'Mike': 95
}
try:
    a=input('Введите имя: ')
    ocenka=students[a]
    number=int(input('Делитель: '))
    if number==0:
        raise ZeroDivisionError('Число дожно быть больше нуля')
except KeyError:
    print('Студент не найден')
except ValueError as error:
    print(error)
else: print(ocenka/number)
finally: print('Программа завершена')

    
    
