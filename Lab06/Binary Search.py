class Student:
    def __init__(self, std_id, name,gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        return self.std_id

    def get_name(self):
        return self.name

    def get_gpa(self):
        return self.gpa

    def print_details(self):
        print(f"ID: {self.get_std_id()}")
        print(f"Name: {self.get_name()}")
        print(f"GPA: {self.get_gpa():.2f}")

def binary_search(data,target):
    begin = 0
    end = len(data) - 1
    compare=0
    while begin <= end:
        mid = (begin + end) // 2
        compare += 1
        if target > data[mid].get_name():
            begin = mid + 1
        elif target < data[mid].get_name():
            end = mid - 1
        else:
            print(f"Found {data[mid].get_name()} at index {mid}")
            data[mid].print_details()
            return (f"Comparisons times: {compare}")
    return f"{target} does not exists.\nComparisons times: {compare}"

def main(text_in, name):
    import json
    std_in = json.loads(text_in)
    data = list()
    for i in std_in:
        std = Student(i["id"], i["name"], i["gpa"])
        data.append(std)
    print(binary_search(data, name))
main(input(), input())
