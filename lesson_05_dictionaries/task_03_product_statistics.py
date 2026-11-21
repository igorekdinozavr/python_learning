products = {
    'mouse': {'price': 2999, 'count': 3},
    'keyboard': {'price': 1999, 'count': 2},
    'monitor': {'price': 12999, 'count': 5},
    'processor': {'price': 8999, 'count': 1},
    'server': {'price': 6799, 'count': 1}
}

total = 0
count = 0
max_price = 0
max_name = ''

for key, value in products.items():
    a = value['price'] * value['count']
    print(key, a)

    if value['price'] > max_price:
        max_name = key
        max_price = value['price']

    total = total + a
    count += 1

print('Сумма:', total)
print('Кол-во товаров:', count)
print('Самый дорогой товар:', max_name)
print('Максимальная цена:', max_price)
