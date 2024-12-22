class ArrayStack():
    def __init__(self):
        self.data = list()
        self.copyData = list()
        self.printStack = list()

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

    def pushPrint(self,group,round,total_round):
        x = 0
        for i in self.copyData:
            if x == group:
                x = 0
            if not x:
                self.printStack.append(i)
            x += 1

        print(f"Group {round}: ",end="")
        check = 0
        for j in self.printStack:
            check += 1
            if check < len(self.printStack):
                print(j+', ',end="")
            else:
                print(j,end="\n")

    def clearPop(self):
        for _ in range(len(self.printStack)):
            if self.printStack:
                self.printStack.pop()

        if self.copyData:
            for i in range(len(self.copyData)):
                x = self.copyData.pop()
                self.data.append(x)
            self.data.pop()

    def popInput(self):
        if self.data:
            x = self.data.pop()
            self.copyData.append(x)       
        
def main():
    stack = ArrayStack()
    group = int(input())
    total_s = int(input())
    for _ in range(total_s):
        text_in = input()
        stack.push(text_in)
    for _ in range(total_s):
        stack.popInput()
    for i in range(1,group+1):
        stack.pushPrint(group,i,total_s)
        stack.clearPop()
        if i < group:
            for _ in range(total_s):
                stack.popInput()
main()
