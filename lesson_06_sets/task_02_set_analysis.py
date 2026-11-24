users_site = {'Alex', 'John', 'Kate', 'Mike', 'Anna', 'David'}
users_app = {'Kate', 'Mike', 'Anna', 'Peter', 'David'}
users_paid = {'Alex', 'Kate', 'Anna', 'David'}

print('Пользователи сайта и приложения:', users_site | users_app)
print('Пользователи и сайта и приложения:', users_site & users_app)
print('Используют сайт, но не приложение:', users_site - users_app)
print('Используют оба сервиса и подписку:', users_site & users_app & users_paid)
print('Количество использующих оба сервиса:', len(users_site & users_app))
