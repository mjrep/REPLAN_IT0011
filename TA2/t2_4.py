file = open('students.txt', 'r')
print("Reading Student Information: ")
for line in file:
    print(line, end = "")
file.close()