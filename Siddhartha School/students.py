""" import json

# Function to load the database from a JSON file
def load_database():
    with open("dbsbss.json", "r") as file:
        return json.load(file)

# Function to save the database to a JSON file
def save_database(data):
    with open("dbsbss.json", "a") as file:
        json.dump(data, file, indent=4)

# Function to greet the user
def greet_user():
    print("Welcome to Siddhartha Boarding School System!")

# Function for student-specific actions
def student_actions(student_id, db):
    student = next((s for s in db["students"] if s["id"] == student_id), None)
    if student:
        print(f"Your details: {student}")
        teacher = next((t for t in db["teachers"] if t["id"] == student["teacher_id"]), None)
        if teacher:
            print(f"Assigned Teacher: {teacher['name']}")
        print(f"Friends: {', '.join(student['friends'])}")
    else:
        print("Student not found.")

# Function for parent-specific actions
def parent_actions(db):
    print("Parent Actions:")
    print("1. Add student records")
    print("2. View grades")
    choice = input("Enter your choice: ")
    if choice == "1":
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        teacher_id = input("Enter assigned teacher ID: ")
        friends = input("Enter friends (comma-separated): ").split(",")
        new_student = {
            "id": student_id,
            "name": student_name,
            "teacher_id": teacher_id,
            "friends": friends
        }
        db["students"].append(new_student)
        save_database(db)
        print("Student record added successfully.")
    elif choice == "2":
        student_id = input("Enter student ID to view grades: ")
        student = next((s for s in db["students"] if s["id"] == student_id), None)
        if student:
            print(f"Grades for {student['name']}: {student.get('grades', 'No grades available')}")
        else:
            print("Student not found.")
    else:
        print("Invalid choice.")

# Function for teacher-specific actions
def teacher_actions(db):
    print("Teacher Actions:")
    print("1. View student details")
    print("2. View salary structure")
    choice = input("Enter your choice: ")
    if choice == "1":
        student_id = input("Enter student ID to view details: ")
        student = next((s for s in db["students"] if s["id"] == student_id), None)
        if student:
            print(f"Student Details: {student}")
        else:
            print("Student not found.")
    elif choice == "2":
        teacher_id = input("Enter your teacher ID: ")
        teacher = next((t for t in db["teachers"] if t["id"] == teacher_id), None)
        if teacher:
            print(f"Salary Structure: {teacher.get('salary', 'No salary details available')}")
        else:
            print("Teacher not found.")
    else:
        print("Invalid choice.")

# Function for admin-specific actions
def admin_actions(db):
    print("Admin Actions:")
    print("1. Add a new student")
    print("2. Add a new teacher")
    print("3. Delete a student")
    print("4. Delete a teacher")
    choice = input("Enter your choice: ")
    if choice == "1":
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        teacher_id = input("Enter assigned teacher ID: ")
        friends = input("Enter friends (comma-separated): ").split(",")
        new_student = {
            "id": student_id,
            "name": student_name,
            "teacher_id": teacher_id,
            "friends": friends
        }
        db["students"].append(new_student)
        save_database(db)
        print("Student added successfully.")
    elif choice == "2":
        teacher_name = input("Enter teacher name: ")
        teacher_id = input("Enter teacher ID: ")
        salary = input("Enter salary: ")
        new_teacher = {
            "id": teacher_id,
            "name": teacher_name,
            "salary": salary
        }
        db["teachers"].append(new_teacher)
        save_database(db)
        print("Teacher added successfully.")
    elif choice == "3":
        student_id = input("Enter student ID to delete: ")
        db["students"] = [s for s in db["students"] if s["id"] != student_id]
        save_database(db)
        print("Student deleted successfully.")
    elif choice == "4":
        teacher_id = input("Enter teacher ID to delete: ")
        db["teachers"] = [t for t in db["teachers"] if t["id"] != teacher_id]
        save_database(db)
        print("Teacher deleted successfully.")
    else:
        print("Invalid choice.")

# Main function to run the program
def main():
    db = load_database()
    greet_user()
    while True:
        print("\nSelect your role:")
        print("1. Student")
        print("2. Parent")
        print("3. Teacher")
        print("4. Admin")
        print("5. Exit")
        role = input("Enter your role: ")
        if role == "1":
            student_id = input("Enter your student ID: ")
            student_actions(student_id, db)
        elif role == "2":
            parent_actions(db)
        elif role == "3":
            teacher_actions(db)
        elif role == "4":
            admin_actions(db)
        elif role == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid role. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
"""

import json

# Function to load the database from a JSON file
def load_database():
    with open("dbsbss.json", "r") as file:
        return json.load(file)

# Function to save the database to a JSON file
def save_database(data):
    with open("dbsbss.json", "w") as file:
        json.dump(data, file, indent=4)

# Function to greet the user
def greet_user():
    print("\nGood Morning!! \nWelcome to Siddhartha Boarding School System!")

# Function for student-specific actions
def student_actions(student_id, db):
    student = next((s for s in db["students"] if s["id"] == student_id), None)
    if student:
        print(f"Your details: {student}")
        teacher = next((t for t in db["teachers"] if t["id"] == student["teacher_id"]), None)
        if teacher:
            print(f"Assigned Teacher: {teacher['name']}")
        print(f"Friends: {', '.join(student['friends'])}")
    else:
        print("Student not found.")

# Function for parent-specific actions
def parent_actions(db):
    print("The followings are the available Parent Actions:")
    print("1. Add student records")
    print("2. View grades")
    choice = input("Enter your choice: ")
    if choice == "1":
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        teacher_id = input("Enter assigned teacher ID: ")
        friends = input("Enter friends (comma-separated): ").split(",")
        new_student = {
            "id": student_id,
            "name": student_name,
            "teacher_id": teacher_id,
            "friends": friends
        }
        db["students"].append(new_student)
        save_database(db)
        print("Student record added successfully.")
    elif choice == "2":
        student_id = input("Enter student ID to view grades: ")
        student = next((s for s in db["students"] if s["id"] == student_id), None)
        if student:
            print(f"Grades for {student['name']}: {student.get('grades', 'No grades available')}")
        else:
            print("Student not found.")
    else:
        print("Invalid choice. Please retry with a valid request!")

# Function for teacher-specific actions
def teacher_actions(db):
    print("Teacher Actions:")
    print("1. View student details")
    print("2. View salary structure")
    choice = input("Enter your choice: ")
    if choice == "1":
        student_id = input("Enter student ID to view details: ")
        student = next((s for s in db["students"] if s["id"] == student_id), None)
        if student:
            print(f"Student Details: {student}")
        else:
            print("Student not found.")
    elif choice == "2":
        teacher_id = input("Enter your teacher ID: ")
        teacher = next((t for t in db["teachers"] if t["id"] == teacher_id), None)
        if teacher:
            print(f"Salary Structure: {teacher.get('salary', 'No salary details available')}")
        else:
            print("Teacher not found.")
    else:
        print("Invalid choice.")

# Function for admin-specific actions
def admin_actions(db):
    print("Admin Actions:")
    print("1. Add a new student")
    print("2. Add a new teacher")
    print("3. Delete a student")
    print("4. Delete a teacher")
    choice = input("Enter your choice: ")
    if choice == "1":
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        teacher_id = input("Enter assigned teacher ID: ")
        friends = input("Enter friends (comma-separated): ").split(",")
        new_student = {
            "id": student_id,
            "name": student_name,
            "teacher_id": teacher_id,
            "friends": friends
        }
        db["students"].append(new_student)
        save_database(db)
        print("Student added successfully.")
    elif choice == "2":
        teacher_name = input("Enter teacher name: ")
        teacher_id = input("Enter teacher ID: ")
        salary = input("Enter salary: ")
        new_teacher = {
            "id": teacher_id,
            "name": teacher_name,
            "salary": salary
        }
        db["teachers"].append(new_teacher)
        save_database(db)
        print("Teacher added successfully.")
    elif choice == "3":
        student_id = input("Enter student ID to delete: ")
        db["students"] = [s for s in db["students"] if s["id"] != student_id]
        save_database(db)
        print("Student deleted successfully.")
    elif choice == "4":
        teacher_id = input("Enter teacher ID to delete: ")
        db["teachers"] = [t for t in db["teachers"] if t["id"] != teacher_id]
        save_database(db)
        print("Teacher deleted successfully.")
    else:
        print("Invalid choice.")

# Main function to run the program
def main():
    db = load_database()
    greet_user()
    while True:
        print("\nSelect your role:")
        print("1. Student")
        print("2. Parent")
        print("3. Teacher")
        print("4. Admin")
        print("5. Exit")
        role = input("Enter your role: ")
        if role == "1":
            print("The system is protected so you would need to submit your valid identifications to proceed! ")
            student_id = input("Enter your STUDENT ID: ")
            student_actions(student_id, db)
        elif role == "2":
            parent_actions(db)
        elif role == "3":
            teacher_actions(db)
        elif role == "4":
            admin_actions(db)
        elif role == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid role. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
