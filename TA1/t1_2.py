#2
userInput = input("Enter a string: ")
total = 0

for char in userInput:
    if char.isdigit():
        total += int(char)

print(f"Sum of digits: {total}")