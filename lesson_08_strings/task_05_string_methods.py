text = 'Python is a powerful programming language'
if 'programming' in text:
    print('Programming есть')
print('Количество "a":',text.count('a'))
print('Замена слова:', text.replace('powerful', 'popular'))
a=text.split()
print('Последнее слово:',a[-1])
