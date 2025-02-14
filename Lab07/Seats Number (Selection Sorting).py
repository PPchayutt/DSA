import json

def split_seat(seat):
    letter = seat[0]
    number = int(seat[1:])
    return letter, number

def selection(list, last):
    compare = 0

    for current in range(last):
        smallest = current
        smallest_letter, smallest_num = split_seat(list[smallest])

        for walker in range(current + 1, last + 1):
            walker_letter, walker_num = split_seat(list[walker])
            compare += 1

            if(walker_letter < smallest_letter) or \
            (walker_letter == smallest_letter and walker_num < smallest_num):
                smallest = walker
                smallest_letter, smallest_num = walker_letter, walker_num

        if smallest != current:
            list[current], list[smallest] = list[smallest], list[current]

        print(list)

    print("Comparison times:", compare)

selection(json.loads(input()), int(input()))
