text = 'apple banana apple orange banana apple grape'
words=text.split()
unique_words=set(words)
count=0
max_count=0
name=''
for a in unique_words:
    count+=1
print(count)
for word in unique_words:
    count=words.count(word)
    if max_count<count:
        max_count=count
        name=word
print(name, max_count)
