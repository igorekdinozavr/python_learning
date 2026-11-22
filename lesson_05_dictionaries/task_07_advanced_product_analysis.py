products = {
    'mouse': {'price': 2999, 'count': 10, 'category': 'devices'},
    'keyboard': {'price': 4999, 'count': 5, 'category': 'devices'},
    'monitor': {'price': 15999, 'count': 3, 'category': 'devices'},
    'table': {'price': 7999, 'count': 8, 'category': 'furniture'},
    'chair': {'price': 5999, 'count': 4, 'category': 'furniture'}
}
max_count=0
total=0
devices_count=0
furniture_count=0
max_name=''
for name, value in products.items():
    a=products[name]['price']*products[name]['count']
    total=total+a
    if max_count<value['count']:
        max_count=value['count']
        max_name=name
    if value['category']=='devices':
        devices_count +=1
    elif value['category']=='furniture':
        furniture_count+=1
    if(value['price'])>10000:
        print('Товары дороже 10000: ',name)
        print('Количество:', value['count'])
print('Общая сумма товаров на складе:',total)
print('Больше всего на складе:', max_name)
print('Количество:', max_count)
print('Количество устройств: ', devices_count)
print('Количество мебели: ',furniture_count)
    
