with open('students.txt', 'w') as file:
    file.write('Alex, John')
with open('students.txt', 'a') as file:
    file.write('\nMike, Kate')
with open('students.txt', 'r')as file:
    text=file.read()
    print(text)
