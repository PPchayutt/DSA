import json
def isIntersect(a, b, c):
    a = json.loads(a)
    b = json.loads(b)
    c = json.loads(c)
    for i in a:
        if i in b and i in c:
            print("True")
            return
    print("False")
isIntersect(input(), input(), input())
