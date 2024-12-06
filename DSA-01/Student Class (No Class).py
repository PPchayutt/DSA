def main():
    name1 = input()
    gender1 = input()
    age1 = int(input())
    id1 = input()
    gpa1 = float(input())
    name2 = input()
    gender2 = input()
    age2 = int(input())
    id2 = input()
    gpa2 = float(input())
    name3 = input()
    gender3 = input()
    age3 = int(input())
    id3 = input()
    gpa3 = float(input())
    search_id = input()
    if search_id == id1:
        prefix = "Mr" if gender1 == "Male" else "Miss"
        print(f"{prefix} {name1} ({age1}) ID: {id1} GPA {gpa1:.2f}")
    elif search_id == id2:
        prefix = "Mr" if gender2 == "Male" else "Miss"
        print(f"{prefix} {name2} ({age2}) ID: {id2} GPA {gpa2:.2f}")
    elif search_id == id3:
        prefix = "Mr" if gender3 == "Male" else "Miss"
        print(f"{prefix} {name3} ({age3}) ID: {id3} GPA {gpa3:.2f}")
    else:
        print("Student not found")
main()
