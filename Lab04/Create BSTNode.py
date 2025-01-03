class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """
        self.data = data
        self.left = None
        self.right = None

def main():
    """ > 3 < """ 
    p_new = BSTNode(input())
    print(p_new.data)
    print(p_new.left)
    print(p_new.right)
main()
