orders = {
    'order_1': {'mouse', 'keyboard', 'monitor'},
    'order_2': {'mouse', 'laptop'},
    'order_3': {'keyboard', 'mouse'},
    'order_4': {'monitor', 'laptop'},
    'order_5': {'mouse', 'keyboard', 'laptop'}
}
products=set()
for name, value in orders.items():
    products=(value|products)
print(products)
for name, value in orders.items():
    if 'mouse' in value:
        print('Найден заказ')
        print(name)
for name, value in orders.items():
    if 'mouse' in value and 'keyboard' in value:
        print('Найден заказ')
        print(name)
a=set(orders['order_1'])
b=set(orders['order_5'])
print(a-b)
с=orders['order_1'] | orders['order_2'] | orders['order_3'] | orders['order_4'] | orders['order_5']
for name in c:
    if name in orders['order_1'] and name in orders['order_2']and name in orders['order_3']and name in orders['order_4']and name in orders['order_5']:
        print(name)
    else:
        print('Такого товара нет')
