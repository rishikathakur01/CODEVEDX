import json
import os

class StudentManagement:
    def __init__(self, data_file="student_records.json"):
        self.data_file = data_file
        self.student_grade = self.load_data()

    # File se data load karne ke liye method
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except:
                return {}
        return {}

    # File mein data write karne ke liye method
    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.student_grade, file, indent=4)

    #Add a new student  
    def add_student(self, name, grade):
        self.student_grade[name] = grade
        self.save_data()
        # Example: Entry added for a user
        print(f"-> Successfully registered {name} with score: {grade}")

    #Update a student 
    def modify_student_score(self, name, grade):
        if name in self.student_grade:
            self.student_grade[name] = grade
            self.save_data()
            print(f"-> Data updated: {name} now has {grade} marks") 

        else:
            print(f"{name} is not found in our database!")

    #Delete a student
    def remove_student(self, name):
        if name in self.student_grade:
            del self.student_grade[name]
            self.save_data()
            print(f"{name} has been successfully deleted")

        else:
            print(f"{name} is not found!")

    # Search for a student 
    def search_student(self, name):
        if name in self.student_grade:
            print("\n=====================================")
            print(f"{'STUDENT NAME':<20} | {'GRADE':<10}")
            print("=====================================")
            print(f"{name:<20} | {self.student_grade[name]:<10}")
            print("=====================================")
        else:
            print(f"-> Info: {name} is not found in our database!")

    #View all students
    def show_all_records(self):
        if self.student_grade:
            print("\n=====================================")
            print(f"{'STUDENT NAME':<20} | {'GRADE':<10}")
            print("=====================================")
            for name, grade in self.student_grade.items():
                print(f"{name:<20} | {grade:<10}")
            print("=====================================")

        else:
            print("No students found/added")

def main():
    system = StudentManagement()

    while True:
        print('\n Student Grades Managements System')
        print("1. Add Student")
        print("2. Modify Student Score")
        print("3. Remove Student")
        print("4. Search Student")
        print("5. Show All Records")
        print("6. Exit System")

        try:
            choice = int(input("Enter your choice(1-6) = "))
        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            name = input("Enter student name = ")
            try:
                grade = int(input("Enter student grade = "))
                system.add_student(name, grade)
            except ValueError:
                print("Invalid grade! Please enter a number.")

        elif choice == 2:
            name = input("Enter student name = ")
            try:
                grade = int(input("Enter student grade = "))
                system.modify_student_score(name, grade)
            except ValueError:
                print("Invalid grade! Please enter a number.")

        elif choice == 3:
            name = input("Enter student name = ")
            system.remove_student(name)

        elif choice == 4:
            name = input("Enter student name to search = ")
            system.search_student(name)

        elif choice == 5:
            system.show_all_records()

        elif choice == 6:
            print("Disconnecting from system...")
            break

        else:
            print("Invalid choice! Please choose between 1 and 6.")

if __name__ == "__main__":
    main()
