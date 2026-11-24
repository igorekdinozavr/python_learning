
orders = {
    'Alex': ['mouse', 'keyboard', 'mouse'],
    'John': ['monitor', 'mouse'],
    'Kate': ['keyboard', 'laptop', 'mouse'],
    'Mike': ['monitor', 'laptop']
}

all_products = set()

for name, value in orders.items():
    products = set(value)
    all_products = all_products | products

print('Все товары:', all_products)


print('\nПокупатели laptop:')

for name, value in orders.items():
    products = set(value)
    if 'laptop' in products:
        print(name)


alex = set(orders['Alex'])
kate = set(orders['Kate'])

print('\nОбщие товары Alex и Kate:', alex & kate)


john = set(orders['John'])
mike = set(orders['Mike'])

print('\nТовары John, которых нет у Mike:', john - mike)
