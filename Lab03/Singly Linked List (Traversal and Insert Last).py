class DataNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
    
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

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    mylist.insert_last(input())
  mylist.traverse()
main()
