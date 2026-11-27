import random
import datetime
now=datetime.datetime.now()
numbers=[32,43,675,86,42,87,89,23,84,40]
a=random.sample(numbers,3)
print (now.strftime('%Y-%m-%d'))
print(a)
