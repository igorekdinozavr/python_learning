with open('scores.txt', 'r') as file:
    lines=file.readlines()
    summa=0
    count=0
    print('Написали выше 85 баллов:')
    for i in lines:
        a=i.split()
        score=int(a[1])
        if score>85:
            print(a[0])
            count+=1
            summa=summa+int(a[1])
    print('Написавших на балл выше 85', count)
    print('Сумма баллов студентов', summa)
    print('Средний балл студента', summa/count)
