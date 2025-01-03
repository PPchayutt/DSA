class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """
        self.data = data
        self.left = None
        self.right = None
    
    def get_data(self):
        return self.data
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
            return
        
        def insert_recursive(node, value):
            if node is None:
                return BSTNode(value)
            
            if value < node.data:
                node.left = insert_recursive(node.left, value)
            else:
                node.right = insert_recursive(node.right, value)
            
            return node
        
        self.root = insert_recursive(self.root, data)

    def preorder(self):
        def preorder_recursive(node):
            if node is not None:
                print("->", node.get_data(), end=" ")
                preorder_recursive(node.get_left())
                preorder_recursive(node.get_right())
        
        preorder_recursive(self.root)

    def inorder(self):
        def inorder_recursive(node):
            if node is not None:
                inorder_recursive(node.get_left())
                print("->", node.get_data(), end=" ")
                inorder_recursive(node.get_right())
        
        inorder_recursive(self.root)

    def postorder(self):
        def postorder_recursive(node):
            if node is not None:
                postorder_recursive(node.get_left())
                postorder_recursive(node.get_right())
                print("->", node.get_data(), end=" ")
        
        postorder_recursive(self.root)

    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
            return
        
        print("Preorder: ", end="")
        self.preorder()
        print()
        
        print("Inorder: ", end="")
        self.inorder()
        print()
        
        print("Postorder: ", end="")
        self.postorder()

    def find_min(self):
        if self.is_empty():
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def find_max(self):
        if self.is_empty():
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data
    
    def delete(self, data):
        self.deleted_value = None

        def delete_recursive(node, value):
            if node is None:
                return None
            if value < node.data:
                node.left = delete_recursive(node.left, value)
            elif value > node.data:
                node.right = delete_recursive(node.right, value)
            else:
                self.deleted_value = node.data
                
                if node.left is None and node.right is None:
                    return None
                    
                if node.right is None:
                    return node.left
                    
                if node.left is None:
                    return node.right
                    
                max_left = node.left
                while max_left.right:
                    max_left = max_left.right
                    
                node.data = max_left.data
                node.left = delete_recursive(node.left, max_left.data)
            
            return node
        
        self.root = delete_recursive(self.root, data)
        
        if self.deleted_value is None:
            print(f"Delete Error, " + data + " is not found in Binary Search Tree.")
            return None
            
        return self.deleted_value

def main():
  my_bst = BST()
  while 1:
    text = input()
    if text == "Done":
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse()
main()
