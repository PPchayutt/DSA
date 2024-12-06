class Student:
    def __init__(self, name, gender, age, student_id, gpa):
        self.name = name
        self.gender = gender
        self.age = age
        self.student_id = student_id
        self.gpa = gpa
    
    def get_prefix(self):
        return "Mr" if self.gender == "Male" else "Miss"
    
    def display_info(self):
        return f"{self.get_prefix()} {self.name} ({self.age}) ID: {self.student_id} GPA {self.gpa:.2f}"

def main():
    students = [
        Student(input(), input(), int(input()), input(), float(input())),
        Student(input(), input(), int(input()), input(), float(input())),
        Student(input(), input(), int(input()), input(), float(input()))
    ]
    search_id = input()
    found = False
    for student in students:
        if student.student_id == search_id:
            print(student.display_info())
            found = True
            break
    if not found:
        print("Student not found")
main()
