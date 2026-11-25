with open('scores.txt', 'r') as file:
    lines=file.readlines()
    count=0
    summa=0
    for i in lines:
        line=i
        a=line.split()
        print('Имя: ', a[0])
        print('Балл: ', a[1])
        count+=1
        summa=summa+int(a[1])
    print('Средний балл: ', summa/count)
