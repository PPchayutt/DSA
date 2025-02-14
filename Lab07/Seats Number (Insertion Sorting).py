import json

def split_seat(seat):
    letter = seat[0]
    number = int(seat[1:])
    return letter, number

def insertion(list, last):
    compare = 0
    
    for current in range(1, last + 1):
        hold = list[current]
        hold_letter, hold_num = split_seat(hold)
        
        walker = current - 1
        
        while walker >= 0:
            walker_letter, walker_num = split_seat(list[walker])
            
            compare += 1
            
            if walker_letter > hold_letter or \
               (walker_letter == hold_letter and walker_num > hold_num):
                list[walker + 1] = list[walker]
                walker -= 1
            else:
                break
                
        list[walker + 1] = hold
        print(list)
    
    print("Comparison times:", compare)

insertion(json.loads(input()), int(input()))
