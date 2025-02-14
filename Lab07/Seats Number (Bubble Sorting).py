import json

def split_seat(seat):
    letter = seat[0]
    number = int(seat[1:])
    return letter, number

def bubble(list, last):
    compare = 0
    sorted = False
    current = 0

    while current <= last and not sorted:
        sorted = True

        walker = last
        while walker > current:
            current_letter, current_num = split_seat(list[walker])
            prev_letter, prev_num = split_seat(list[walker-1])

            compare += 1

            if (current_letter < prev_letter) or \
            (current_letter == prev_letter and current_num < prev_num):
                list[walker], list[walker-1] = list[walker-1], list[walker]
                sorted = False
            
            walker -= 1

        current += 1
        print(list)

    print("Comparison times:", compare)

bubble(json.loads(input()), int(input()))
