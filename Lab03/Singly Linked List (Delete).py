class DataNode:
    def __init__(self, data):
        self.data = data 
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def delete(self, data):
        if self.head is None:
            print(f"Cannot delete, " + data + " does not exist.")
            return
        if self.head.data == data:
            self.head = self.head.next
            self.count -= 1
            return
        current = self.head
        prev = None
        found = False
        while current is not None:
            if current.data == data:
                found = True
                break
            prev = current
            current = current.next
        if not found:
            print(f"Cannot delete, " + data + " does not exist.")
            return
        prev.next = current.next
        self.count -= 1
    
    def insert_before(self, node, data):
        if self.head is None:
            print("Cannot insert, " + node + " does not exist.")
            return
        if self.head.data == node:
            self.insert_front(data)
            return
        current = self.head
        prev = None
        found = False
        while current is not None:
            if current.data == node:
                found = True
                break
            prev = current
            current = current.next
        if not found:
            print(f"Cannot insert, " + node + " does not exist.")
            return
        new_node = DataNode(data)
        new_node.next = current
        prev.next = new_node
        self.count += 1

    def insert_front(self, data):
        new_node = DataNode(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
    
    def insert_last(self, data):
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.count += 1

    def traverse(self):
        if self.count == 0:
            print("This is an empty list.")
            return
        current = self.head
        output = str(current.data)
        while current.next is not None:
            current = current.next
            output += " -> " + str(current.data)
        print(output)
        
def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
      mylist.insert_before(*data.split(", "))
    elif condition == "D":
      mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()
main()

