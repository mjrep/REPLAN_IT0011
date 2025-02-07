#1
userInput = input("Enter a string: ")
vowels = 0
consonants = 0
spaces = 0
others = 0

input_string = userInput.lower()

for char in input_string:
    if char in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Spaces: {spaces}")
print(f"Other characters: {others}")