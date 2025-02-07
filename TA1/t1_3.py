print("a.")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end="")
    print()
    
print("\nb.")
i = 1
while i <= 7:
    if i % 2 == 1 or i == 6:
        print(str(i) * i)
    i += 1