orders = {
    'order_1': {'price': 1500, 'count': 2, 'status': 'done'},
    'order_2': {'price': 3000, 'count': 1, 'status': 'pending'},
    'order_3': {'price': 500, 'count': 5, 'status': 'done'},
    'order_4': {'price': 2500, 'count': 3, 'status': 'pending'},
    'order_5': {'price': 1000, 'count': 4, 'status': 'done'}
}
count=0
total=0
summa=0
max_count=0
max_name=0
for name, value in orders.items():
    summa=summa+(value['price']*value['count'])
    if value['status']=='done':
        count+=1
        total=total+(value['price']*value['count'])
    if max_count<(value['price']*value['count']):
        max_count=(value['price']*value['count'])
        max_name=name
    if value['status']=='pending':
        print('Незавершенный заказ: ', name) 
print('Общая стоимость всех заказов: ', summa)
print('Количество выполненных заказов: ', count)
print('Сумма выполненных заказов: ', total)
print(max_name,':', max_count)
