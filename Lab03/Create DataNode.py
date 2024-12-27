class DataNode:
  def __init__(self, data=None):
    self.data = data
    self.next = None

def main():
  data = input()
  node = DataNode(data)
  print(node.data)
  print(node.next)
main()
