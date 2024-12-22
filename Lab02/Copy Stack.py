class ArrayStack:
    def __init__(self, data = []):
        self._size = 0
        self._data = data

    def push(self, data):
        self._data = self._data + [data]
        self._size += 1

    def pop(self):
        if not self._size:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            last_item = self._data[-1]
            del self._data[-1]
            self._size -= 1
            return last_item

    def is_empty(self):
        if not self._size:
            return True
        return False

    def get_stack_top(self):
        if not self._size:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self._data[-1]

    def get_size(self):
        return self._size

    def print_stack(self):
        return print(self._data)
    
STACK1 = ArrayStack()
STACK2 = ArrayStack()
REVERSE_STACK1 = []
STACK1.push(10)
STACK1.push(20)
STACK1.push(30)
STACK2.push(15)

def copyStack():
    while STACK2._data:
        STACK2.pop()
    for _ in range(STACK1.get_size()):
        item = STACK1.pop()
        REVERSE_STACK1.append(item)
    
    while REVERSE_STACK1:
        STACK2.push(REVERSE_STACK1.pop())

    return STACK2.print_stack()
copyStack()
