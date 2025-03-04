import os

# Initialize records list
records = []

while True:
    print("\nMenu:")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Order by Last Name")
    print("6. Order by Grade")
    print("7. Show Student Record")
    print("8. Add Record")
    print("9. Edit Record")
    print("10. Delete Record")
    print("11. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        filename = input("Enter filename: ")
        try:
            with open(filename, 'r') as file:
                for line in file:
                    student_id, first_name, last_name, class_standing, major_exam_grade = line.strip().split(',')
                    records.append({
                        'student_id': student_id,
                        'first_name': first_name,
                        'last_name': last_name,
                        'class_standing': float(class_standing),
                        'major_exam_grade': float(major_exam_grade)
                    })
            print(f"File {filename} opened successfully.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
            
    elif choice == "2":
        filename = input("Enter filename (default: records.txt): ") or "records.txt"
        with open(filename, 'w') as file:
            for record in records:
                file.write(f"{record['student_id']},{record['first_name']},{record['last_name']},{record['class_standing']},{record['major_exam_grade']}\n")
        print(f"Records saved to {filename}.")
        
    elif choice == "3":
        filename = input("Enter filename: ")
        with open(filename, 'w') as file:
            for record in records:
                file.write(f"{record['student_id']},{record['first_name']},{record['last_name']},{record['class_standing']},{record['major_exam_grade']}\n")
        print(f"Records saved to {filename}.")
        
    elif choice == "4":
        if not records:
            print("No records available.")
        else:
            for i, record in enumerate(records, start=1):
                print(f"Record {i}:")
                print(f"Student ID: {record['student_id']}")
                print(f"Name: {record['first_name']} {record['last_name']}")
                print(f"Class Standing: {record['class_standing']}")
                print(f"Major Exam Grade: {record['major_exam_grade']}")
                print(f"Overall Grade: {(record['class_standing'] * 0.6) + (record['major_exam_grade'] * 0.4):.2f}\n")
                
    elif choice == "5":
        sorted_records = sorted(records, key=lambda x: x['last_name'])
        if not sorted_records:
            print("No records available.")
        else:
            for i, record in enumerate(sorted_records, start=1):
                print(f"Record {i}:")
                print(f"Student ID: {record['student_id']}")
                print(f"Name: {record['first_name']} {record['last_name']}")
                print(f"Class Standing: {record['class_standing']}")
                print(f"Major Exam Grade: {record['major_exam_grade']}")
                print(f"Overall Grade: {(record['class_standing'] * 0.6) + (record['major_exam_grade'] * 0.4):.2f}\n")
                
    elif choice == "6":
        sorted_records = sorted(records, key=lambda x: (x['class_standing'] * 0.6) + (x['major_exam_grade'] * 0.4), reverse=True)
        if not sorted_records:
            print("No records available.")
        else:
            for i, record in enumerate(sorted_records, start=1):
                print(f"Record {i}:")
                print(f"Student ID: {record['student_id']}")
                print(f"Name: {record['first_name']} {record['last_name']}")
                print(f"Class Standing: {record['class_standing']}")
                print(f"Major Exam Grade: {record['major_exam_grade']}")
                print(f"Overall Grade: {(record['class_standing'] * 0.6) + (record['major_exam_grade'] * 0.4):.2f}\n")
                
    elif choice == "7":
        student_id = input("Enter Student ID: ")
        for record in records:
            if record['student_id'] == student_id:
                print(f"Student ID: {record['student_id']}")
                print(f"Name: {record['first_name']} {record['last_name']}")
                print(f"Class Standing: {record['class_standing']}")
                print(f"Major Exam Grade: {record['major_exam_grade']}")
                print(f"Overall Grade: {(record['class_standing'] * 0.6) + (record['major_exam_grade'] * 0.4):.2f}")
                break
        else:
            print("Record not found.")
            
    elif choice == "8":
        student_id = input("Enter Student ID (6 digits): ")
        if len(student_id) != 6 or not student_id.isdigit():
            print("Invalid Student ID. Please enter a 6-digit number.")
        else:
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            while True:
                try:
                    class_standing = float(input("Enter Class Standing (0-100): "))
                    if 0 <= class_standing <= 100:
                        break
                    else:
                        print("Invalid grade. Please enter a value between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            while True:
                try:
                    major_exam_grade = float(input("Enter Major Exam Grade (0-100): "))
                    if 0 <= major_exam_grade <= 100:
                        break
                    else:
                        print("Invalid grade. Please enter a value between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            records.append({
                'student_id': student_id,
                'first_name': first_name,
                'last_name': last_name,
                'class_standing': class_standing,
                'major_exam_grade': major_exam_grade
            })
            print("Record added successfully.")
            
    elif choice == "9":
        student_id = input("Enter Student ID: ")
        for record in records:
            if record['student_id'] == student_id:
                print("Enter new details (press Enter to keep current value):")
                record['first_name'] = input(f"Enter First Name ({record['first_name']}): ") or record['first_name']
                record['last_name'] = input(f"Enter Last Name ({record['last_name']}): ") or record['last_name']
                while True:
                    new_class_standing = input(f"Enter Class Standing ({record['class_standing']}): ")
                    if not new_class_standing:
                        break
                    try:
                        new_class_standing = float(new_class_standing)
                        if 0 <= new_class_standing <= 100:
                            record['class_standing'] = new_class_standing
                            break
                        else:
                            print("Invalid grade. Please enter a value between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                while True:
                    new_major_exam_grade = input(f"Enter Major Exam Grade ({record['major_exam_grade']}): ")
                    if not new_major_exam_grade:
                        break
                    try:
                        new_major_exam_grade = float(new_major_exam_grade)
                        if 0 <= new_major_exam_grade <= 100:
                            record['major_exam_grade'] = new_major_exam_grade
                            break
                        else:
                            print("Invalid grade. Please enter a value between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                print("Record updated successfully.")
                break
        else:
            print("Record not found.")
            
    elif choice == "10":
        student_id = input("Enter Student ID: ")
        for record in records:
            if record['student_id'] == student_id:
                records.remove(record)
                print("Record deleted successfully.")
                break
        else:
            print("Record not found.")
            
    elif choice == "11":
        break
        
    else:
        print("Invalid choice. Please choose a valid option.")