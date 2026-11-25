with open ('scores.txt', 'r') as file:
    lines=file.readlines()
    highest=0
    name=''
    for i in lines:
        line=i
        a=line.split()
        if highest<int(a[1]):
            highest=int(a[1])
            name=a[0]
    print('Имя: ', name)
    print('Балл: ', highest)
