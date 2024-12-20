import json
def calculate_score():
    my_list = json.loads(input())
    avg = sum(my_list) / len(my_list)
    larg = my_list[0]
    small = my_list[0]
    for num in my_list:
        if num > larg:
            larg = num
        if num < small:
            small = num
    print(f"({larg}, {small}, {round(avg, 2)})")
calculate_score()
