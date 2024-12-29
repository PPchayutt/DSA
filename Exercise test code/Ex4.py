# def ex_1(n):
#     """
#     ฟังก์ชันคำนวณค่าโดยใช้ recursion:
#     - ถ้า n = 1 จะ return 12
#     - ถ้า n ≠ 1 จะ return n + ex_1(n/2)
#     """
#     if n == 1:
#         return 12
#     else:
#         return n + ex_1(n//2)
# print(ex_1(32))

# def ex_2(n):
#     """
#     ฟังก์ชันที่พิมพ์ข้อความและเรียกตัวเองซ้ำ:
#     - ถ้า n = 8 จะพิมพ์ "Go Back!"
#     - ถ้า n ≠ 8 จะพิมพ์ Hello, เรียกฟังก์ชันด้วย n+2, แล้วพิมพ์ Bye
#     """
#     if n == 8:
#         print("Go Back!")
#     else:
#         print(f"{n} Hello!")
#         ex_2(n + 2)
#         print(f"{n}Bye!")
# ex_2(0)

# def ex_3(x):
#     """
#     ฟังก์ชันคำนวณค่าโดยใช้ recursion:
#     - ถ้า x < 5 จะ return 3*x
#     - ถ้า x ≥ 5 จะ return 2*ex_3(x-5)+7
#     """
#     if x < 5:
#         return 3 * x
#     else:
#         return 2 * ex_3(x - 5) + 7
#     print("Finish!!")
#     return 1
# print(ex_3(4))
# print(ex_3(10))
# print(ex_3(17))
