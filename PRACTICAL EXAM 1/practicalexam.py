excluding_words = ["and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"]

statement = input("Enter a string statement\n:")

words = statement.split()
word_count = {}

for word in words:
    word = word.strip(",.?!")
    
    if word.lower() not in excluding_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
lowercase_word = []
uppercase_word = []

for word in word_count:
    if word[0].islower():
        lowercase_word.append(word)
    else:
        uppercase_word.append(word)

lowercase_word.sort()
uppercase_word.sort()

max_length = 0
for word in word_count:
    if len(word) > max_length:
        max_length = len(word)
        
for word in lowercase_word:
    spaces = " " * (max_length - len(word) + 2)
    print(word + spaces + "- " + str(word_count[word]))
for word in uppercase_word:
    spaces = " " * (max_length - len(word) + 2)
    print(word + spaces + "- " + str(word_count[word]))

total_words = sum(word_count.values())
print("\nTotal words filtered: ",total_words)

