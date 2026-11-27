students = {
    'Alex': 85,
    'John': 90,
    'Kate': 78
}
try:
    a=input('Имя студента: ')
    grade=students[a]
except KeyError:
    print('Студента не существует')
else:
    print(grade)
finally: print('Проверка завершена')
