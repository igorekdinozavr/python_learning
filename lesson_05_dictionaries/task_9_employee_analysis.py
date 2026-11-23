employees = {
    'Alex': {'salary': 50000, 'department': 'IT'},
    'John': {'salary': 40000, 'department': 'Sales'},
    'Kate': {'salary': 70000, 'department': 'IT'},
    'Mike': {'salary': 35000, 'department': 'Sales'},
    'Anna': {'salary': 60000, 'department': 'IT'}
}
total=0
max_salary=0
count_it=0
count_sales=0
middle=0
max_employee=''
for name, value in employees.items():
    if name in employees:
        total=total+value['salary']
    if max_salary<value['salary']:
        max_salary=value['salary']
        max_employee=name
    if value['department']=='IT':
        count_it+=1
    else:
        count_sales+=1
    employees1=(count_it+count_sales)
    middle=total/employees1
print('Средняя зарплата:', middle)
print('Сумма зарплат:', total)
print('Наибольшая зарплата:', max_employee, max_salary)
print('Сотрудников IT:', count_it)
print('Сотрудников Sales:', count_sales)
for name, value in employees.items():
    if value['salary']>middle:
        print ('Зарплата выше среднего:', name, value['salary'])
