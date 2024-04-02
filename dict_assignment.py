word_count = {}
text = "Later in the course, you'll see how to use the collections Counter class."
string = ''
for key in text:
    if key.isalnum():
        word_count[key] = word_count.setdefault(key, 0) + 1
print(word_count)

for letter, count in sorted(word_count.items()):
    print(letter, count)
