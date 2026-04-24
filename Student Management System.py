# Student Management System (CLI)

import json
import os

FILE_NAME = "students.json"


# Load data from file
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


# Add student
def add_student(data):
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {
        "id": sid,
        "name": name,
        "marks": marks
    }

    data.append(student)
    save_data(data)
    print("Student added.")


# View students
def view_students(data):
    if not data:
        print("No records found.")
    else:
        print("\nStudent List:")
        for s in data:
            print(s["id"], "-", s["name"], "-", s["marks"])


# Update student
def update_student(data):
    sid = input("Enter Student ID to update: ")

    for s in data:
        if s["id"] == sid:
            s["name"] = input("Enter new name: ")
            s["marks"] = input("Enter new marks: ")
            save_data(data)
            print("Student updated.")
            return

    print("Student not found.")


# Delete student
def delete_student(data):
    sid = input("Enter Student ID to delete: ")

    for s in data:
        if s["id"] == sid:
            data.remove(s)
            save_data(data)
            print("Student deleted.")
            return

    print("Student not found.")


# Main program
data = load_data()

while True:
    print("\n--- Student Management Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student(data)

    elif choice == '2':
        view_students(data)

    elif choice == '3':
        update_student(data)

    elif choice == '4':
        delete_student(data)

    elif choice == '5':
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")