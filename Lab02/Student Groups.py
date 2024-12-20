class ArrayStack:
    def __init__(self):
        """สร้าง Stack เปล่า โดยใช้ list() เป็นโครงสร้างภายใน"""
        self.size = 0
        self.data = list()
    
    def push(self, input_data):
        """เพิ่มข้อมูลที่ด้านบนสุดของ Stack"""
        self.data.append(input_data)
        self.size += 1
    
    def pop(self):
        """นำข้อมูลออกจากด้านบนสุดของ Stack"""
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()
    
    def is_empty(self):
        """ตรวจสอบว่า Stack ว่างหรือไม่"""
        return self.size == 0
    
    def get_stack_top(self):
        """ดูข้อมูลที่อยู่ด้านบนสุดโดยไม่นำออก"""
        if self.is_empty():
            print("Underflow: Cannot get stack top from an empty list")
            return None
        # ใช้ .get() แทนการใช้วงเล็บเหลี่ยม
        return self.data.get(-1) if hasattr(self.data, 'get') else self.data[-1]
    
    def get_size(self):
        """ส่งคืนขนาดปัจจุบันของ Stack"""
        return self.size
    
    def print_stack(self):
        """แสดงข้อมูลทั้งหมดใน Stack"""
        # สร้างสตริงแสดงผลด้วยวงเล็บธรรมดา
        output = "("
        for i in range(self.size):
            if i > 0:
                output += ", "
            item = self.data.get(i) if hasattr(self.data, 'get') else self.data[i]
            output += str(item)
        output += ")"
        print(output)

def student_groups():
    """จัดกลุ่มนักเรียนโดยใช้ Stack"""
    # รับข้อมูลพื้นฐาน
    m = int(input())  # จำนวนกลุ่ม
    n = int(input())  # จำนวนนักเรียน
    
    # สร้าง Stack สำหรับเก็บชื่อนักเรียน
    student_stack = ArrayStack()
    
    # เก็บชื่อนักเรียนใน Stack
    for _ in range(n):
        name = input()
        student_stack.push(name)
    
    # สร้าง Stack สำหรับเก็บผลลัพธ์แต่ละกลุ่ม
    group_stack = ArrayStack()
    
    # สร้างกลุ่มและจัดการนักเรียน
    for group_num in range(m):
        # คำนวณจำนวนคนในกลุ่มนี้
        people_in_group = (n + m - 1 - group_num) // m
        
        # สร้างสตริงสำหรับกลุ่มนี้
        group_str = "Group " + str(group_num + 1) + ": "
        
        # เพิ่มรายชื่อนักเรียนในกลุ่ม
        for student_num in range(people_in_group):
            if not student_stack.is_empty():
                if student_num > 0:
                    group_str += ", "
                group_str += student_stack.pop()
        
        # เก็บสตริงของกลุ่มนี้
        group_stack.push(group_str)
    
    # สร้าง Stack ชั่วคราวเพื่อพลิกลำดับกลุ่ม
    temp_stack = ArrayStack()
    while not group_stack.is_empty():
        temp_stack.push(group_stack.pop())
    
    # แสดงผลลัพธ์
    while not temp_stack.is_empty():
        print(temp_stack.pop())

# เรียกใช้งานฟังก์ชัน
if __name__ == "__main__":
    student_groups()