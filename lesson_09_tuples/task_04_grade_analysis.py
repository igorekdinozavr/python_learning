grades = (5, 4, 3, 5, 2, 4, 5, 3, 5)
print(len(grades))
count_five=0
count_four=0
max_grade=0
min_grade=0
summa=0
for five in grades:
    if five==5:
        count_five+=1
    if five==4:
        count_four+=1
max_grade=max(grades)
min_grade=min(grades)
summa=sum(grades)
print(summa/len(grades))
ocenka=list()
for i in grades:
    if i ==5:
        ocenka.append(i)
print(ocenka)
