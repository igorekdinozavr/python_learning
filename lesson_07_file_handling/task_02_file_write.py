with open('students.txt', 'w') as file:
    file.write('Alex, John, Kate')
with open('students.txt', 'r') as file:
    text=file.read()
    print(text)
