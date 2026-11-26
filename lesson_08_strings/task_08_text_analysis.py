text = 'Python is easy. Python is powerful. Python is popular.'
text=text.lower()
text=text.replace('.', '')
words=text.split()
unique_words=set(words)
count_unique=0
count=0
name=''
max_count=0
for i in words:
    count+=1
for a in unique_words:
    count_unique+=1
for word in unique_words:
    if max_count<words.count(word):
        max_count=words.count(word)
        name=word
print(name,':', max_count)
    
