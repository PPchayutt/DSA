class ArrayStack:
    def __init__(self):
        self.data = list()
        self.temp_data = list()
        self.display_data = list()

    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)

    def distribute_to_groups(self, group_number, current_group, total_students):
        position = 0
        for student in self.temp_data:
            if position == group_number:
                position = 0
            if position == 0:
                self.display_data.append(student)
            position += 1

        print(f"Group {current_group}: ", end="")
        for i, student in enumerate(self.display_data, 1):
            if i < len(self.display_data):
                print(f"{student}, ", end="")
            else:
                print(student)

    def reset_data(self):
        self.display_data.clear()
        if self.temp_data:
            while self.temp_data:
                self.data.append(self.temp_data.pop())
            self.data.pop()

    def prepare_data(self):
        if self.data:
            student = self.data.pop()
            self.temp_data.append(student)

def manage_student_groups():
    student_stack = ArrayStack()

    number_of_groups = int(input())
    total_students = int(input())

    for _ in range(total_students):
        name = input()
        student_stack.push(name)

    for _ in range(total_students):
        student_stack.prepare_data()

    for group in range(1, number_of_groups + 1):
        student_stack.distribute_to_groups(number_of_groups, group, total_students)
        student_stack.reset_data()

        if group < number_of_groups:
            for _ in range(total_students):
                student_stack.prepare_data()

if __name__ == "__main__":
    manage_student_groups()
