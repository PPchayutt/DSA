import json

def bubble(list, last):
    current = 0
    compare = 0
    sorted = False

    while current <= last and not sorted:
        walker = last
        sorted = True

        while walker > current:
            compare += 1
            if list[walker] < list[walker-1]:
                list[walker], list[walker-1] = list[walker-1], list[walker]
                sorted = False
            walker -= 1

        current += 1
        print(list)

    print("Comparison times:", compare)

bubble(json.loads(input()), int(input()))
