first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
full_name = first_name + " " + last_name
sliced_name = first_name[0:3]
greeting = "Hello, {}! Welcome. You are {} years old."
print("Full name: ", full_name)
print("Sliced name: ",sliced_name)
print("Greeting Message: ",greeting.format(sliced_name,age))
