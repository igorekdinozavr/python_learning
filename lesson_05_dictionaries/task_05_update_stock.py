products = {
    'mouse': {'price': 2999, 'count': 3},
    'keyboard': {'price': 1999, 'count': 2},
    'monitor': {'price': 12999, 'count': 5},
    'processor': {'price': 8999, 'count': 1},
    'server': {'price': 6799, 'count': 1}
}
name=input('Название: ')
if name in products:
    a=int(input('Новое количество: '))
    products[name]['count']=a
    print('Товар: ', name)
    print('Цена: ', products[name]['price']) 
    print('Количество: ', a)
else:
    print ('Товар не найден.')
