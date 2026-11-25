try:
    with open('scores.txt', 'r') as file:
        lines=file.readlines()
        max_score=0
        name=''
        count=0
        summa=0
        for i in lines:
            a=i.split()
            count+=1
            summa=summa+int(a[1])
            if max_score<int(a[1]):
                max_score=int(a[1])
                name=a[0]
    print('Количество студентов:', count)
    print('Общая сумма оценок:', summa)
    print('Максимальная оценка:', max_score, 'Имя студента:', name)
except FileNotFoundError:
    print('Файл не найден')
  
