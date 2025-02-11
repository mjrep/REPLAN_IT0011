file = open("numbers.txt", "r")  
lines = file.readlines()  
file.close()  

line_number = 1  
for line in lines:  
    numbers = line.replace("\n", "").split(",")  # Remove newline and split by comma  
    total = 0  
    
    for num in numbers:  
        num = num.strip()  # Remove any extra spaces
        if num.isdigit():  # Check if it's a valid number
            total += int(num)

    if str(total) == str(total)[::-1]:  
        print(f"Line {line_number}: {', '.join(numbers)} (sum {total}) - Palindrome")  
    else:  
        print(f"Line {line_number}: {', '.join(numbers)} (sum {total}) - Not a palindrome")  

    line_number += 1  
