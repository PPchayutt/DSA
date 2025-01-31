def calcount():
    amount = int(input())
    count = 0
    for i in range(1,amount+1):
        count += len(str(i)) + 1
    print(count)
calcount()
