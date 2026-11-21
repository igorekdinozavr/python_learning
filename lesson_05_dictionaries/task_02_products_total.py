products = {
    'mouse': {'price': 2999, 'count': 3},
    'keyboard': {'price': 1999, 'count': 2},
    'monitor': {'price': 12999, 'count': 5},
    'processor': {'price': 8999, 'count': 1},
    'server': {'price': 6799, 'count': 1}
}

total = 0

for key, value in products.items():
    a = value['price'] * value['count']
    print(key, a)
    total = total + a

print(total)
