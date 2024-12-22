class ArrayStack():
    def __init__(self):
        self.size = 0
        self.data = list()

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
            self.size += 1

    def pop(self):
        if self.data:
            last = self.data.pop()
            self.size -= 1
            return last
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        if not self.data:
            return True
        return False

    def get_stack_top(self):
        if self.data:
            top_element = self.data.pop()
            self.data.append(top_element)
            return top_element
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None

    def get_size(self):
        return len(self.data)

    def print_stack(self):
        print(self.data)

def is_parentheses_matching():
    stack = ArrayStack()
    text = input()
    check = True

    for i in text:
        if i == "(":
            stack.push("(")
        if i == ")":
            if stack.pop() == None:
                check = False

    if not check or stack.get_size():
        print(f"Parentheses in {text} are unmatched")
        print("False")
    else:
        print(f"Parentheses in {text} are matched")
        print("True")

is_parentheses_matching()
