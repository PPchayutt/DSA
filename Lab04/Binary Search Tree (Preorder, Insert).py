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

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    
    print("Preorder: ", end="")
    my_bst.preorder()

main()
