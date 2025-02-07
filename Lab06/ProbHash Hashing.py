class Student:
    def __init__(self, std_id_in, name, gpa):
        self.std_id = std_id_in
        self.name = name
        self.gpa = gpa

    def print_details(self):
        print(f"ID: {self.std_id}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa:.2f}")

class ProbHash:
    def __init__(self, cap):
        self.hash_table = cap * [None]
        self.size = cap
    
    def hash_function(self, input_key):
        return input_key % self.size
    
    def rehash_function(self, hashkey):
        return (hashkey + 1) % self.size
    
    def insert_data(self, std_object: Student):
        std_id_key = std_object.get_std_id()
        hashkey = self.hash_function(std_id_key)
        while self.hash_table[hashkey] != None:
            hashkey = self.rehash_function(hashkey)
        self.hash_table[hashkey] = std_object
        print("Insert", std_id_key, "at index", hashkey)

    def search_data(self, std_id):
        pass


def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
