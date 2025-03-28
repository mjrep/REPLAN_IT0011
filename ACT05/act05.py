def divide(a, b):
    return a / b if b != 0 else None
def exponentiation(a, b):
    return a ** b
def remainder(a, b):
    return a % b if b != 0 else None
def summation(a, b):
    if b <= a:
        return None
    return sum([x for x in range(int(a), int(b)+1)]) if (a.is_integer() and b.is_integer()) else None

while True:
    print("\n[D] Division")
    print("[E] Exponentiation")
    print("[R] Remainder")
    print("[F] Summation")
    print("[Q] Quit")
    print("-------------------------")

    choice = input("Enter choice: ").upper()

    if choice == "Q":
        print("Thank you for using the program")
        break

    if choice not in ["D", "E", "R", "F"]:
        print("Error, Invalid input choice")
        continue 

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        result = None
    else:
        if choice == "D":
            result = divide(num1, num2)
        elif choice == "E":
            result = exponentiation(num1, num2)
        elif choice == "R":
            result = remainder(num1, num2)
        elif choice == "F":
            result = summation(num1, num2)

    print(f"Operation Result: {result if result is not None else 'Invalid input'}")
