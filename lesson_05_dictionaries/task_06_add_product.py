products = {
    'mouse': {'price': 2999, 'count': 3},
    'keyboard': {'price': 1999, 'count': 2},
    'monitor': {'price': 12999, 'count': 5},
    'processor': {'price': 8999, 'count': 1},
    'server': {'price': 6799, 'count': 1}
}
new_product=input('Новый продукт: ')
if new_product not in products:
    a=int(input('Цена: '))
    b=int(input('Количество: '))
    if a<=0 or b<=0: print('Ошибка')
    else:
        products[new_product]={'price': a, 'count':b}
        print('Товар добавлен')
elif new_product in products:
    print ('Товар уже существует.')
for name, value in products.items():
    print (name, value['price'],value['count'])
