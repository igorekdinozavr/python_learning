try:
    with open('scores.txt', 'r') as file:
        lines=file.read()
        print (lines)
except FileNotFoundError:
    print('Файл не найден')
