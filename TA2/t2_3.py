last_name = input("Enter last name: ")
first_name = input("Enter first name: ")
age = input("Enter age: ")
contact_num = input("Enter contact number: ")
course = input("Enter course: ")

data = "Last Name: {}\n" + "First Name: {}\n" + "Age: {}\n" + "Contact Number: {}\n" + "Course: {}"
writeData = data.format(last_name, first_name, age, contact_num, course)

file = open('students.txt', 'w')
file.write(writeData)
file.close()

print("Student information has been saved to 'students.txt'.")

