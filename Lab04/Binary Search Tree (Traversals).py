class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """4
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

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()

main()
