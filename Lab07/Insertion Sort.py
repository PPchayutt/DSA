import json
def insertion(list, last):
    current = 1
    compare = 0
    while current <= last:
        hold = list[current]
        walker = current - 1
        while (walker >= 0 and hold < list[walker]):
            list[walker+1] = list[walker]
            walker -= 1
            compare += 1
        if walker >= 0:
            compare += 1
        list[walker+1] = hold
        current += 1
        print(list)
    print("Comparison times:", compare)

insertion(json.loads(input()), int(input()))
