text = 'Python Java Python C++ Java Python Java'
text=text.split()
print('Количество слов:',len(text))
print('Количество "Python":', text.count('Python'))
for a in text:
    if a=='Java':
        print('Вывод всех слов "Java":', a)
text=set(text)
print(text)
