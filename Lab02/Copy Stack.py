class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = list()
    
    def push(self, input_data):
        self.data.append(input_data)
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()
    
    def is_empty(self):
        return self.size == 0
    
    def get_stack_top(self):
        if self.is_empty():
            print("Underflow: Cannot get stack top from an empty list")
            return None
        temp = self.pop()
        self.push(temp)
        return temp
    
    def get_size(self):
        return self.size
    
def print_stack(self):
    temp_stack = ArrayStack()
    temp_stack2 = ArrayStack()
    output = "["
    is_first = True
    
    while not self.is_empty():
        temp_stack.push(self.pop())
    
    while not temp_stack.is_empty():
        current = temp_stack.pop()
        temp_stack2.push(current)
        
    while not temp_stack2.is_empty():
        current = temp_stack2.pop()
        
        if not is_first:
            output += ", "
            
        if isinstance(current, str):
            output += "'" + str(current) + "'"
        else:
            output += str(current)
            
        is_first = False
        self.push(current)
        
    output += "]"
    print(output)

def copy_stack(stack1, stack2):
    temp_stack = ArrayStack()
    
    while not stack2.is_empty():
        stack2.pop()
    
    while not stack1.is_empty():
        item = stack1.pop()
        temp_stack.push(item)
    
    while not temp_stack.is_empty():
        item = temp_stack.pop()
        stack1.push(item)
        stack2.push(item)

def print_status():
    print("This is stack 1 (%d): " % STACK1_.get_size(), end='')
    STACK1_.print_stack()
    print("This is stack 2 (%d): " % STACK2_.get_size(), end='')
    STACK2_.print_stack()
    print("This is stack 3 (%d): " % STACK3_.get_size(), end='')
    STACK3_.print_stack()
    print("This is stack 4 (%d): " % STACK4_.get_size(), end='')
    STACK4_.print_stack()
    print()

STACK1_ = ArrayStack()
STACK2_ = ArrayStack()
STACK3_ = ArrayStack()
STACK4_ = ArrayStack()

for _ in range(int(input())):
    STACK1_.push(input())

for _ in range(int(input())):
    STACK2_.push(input())

TEMP1_, TEMP2_, TEMP3_, TEMP4_ = id(STACK1_), id(STACK2_), id(STACK3_), id(STACK4_)

print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
print_status()

print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("A")
print_status()

print("Copy Stack 2 to Stack 1")
copy_stack(STACK2_, STACK1_)
STACK2_.push("B")
print_status()

print("Copy Stack 3 to Stack 2")
copy_stack(STACK3_, STACK2_)
STACK3_.push("C")
print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)    
STACK1_.push("D")
print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
STACK2_.push("E")
print_status()

print(TEMP1_ == id(STACK1_), TEMP2_ == id(STACK2_), TEMP3_ == id(STACK3_), TEMP4_ == id(STACK4_))
