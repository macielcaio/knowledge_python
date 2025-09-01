### LOOOPS ###

#for i in range(3):
#  print(i < 1)

#for i in range(3):
#  print("First")
#  print("Second")

#for i in range(3):
#  print("A")
#print("B")
# while teste de loop com break, continue e pass
# temp_f = 40
# while temp_f > 32:
#     print(f"Thw water is {temp_f} degress")
#     temp_f -= 1
#     if temp_f == 33:
#         break
#
# # using continue in a loop for
# for i in range(1,11):
#     if i == 7:
#         print("we skipped 7")
#         continue
#     print(f"this is the number {i}")
#
# # using pass in a loop for
# for i in range(1,11):
#     if i == 3:
#         pass
#     else:
#         print(f"this is the number {i}")
#
#
# check odd and even number from the list
# numbers = [3, 9, 1, 10, 5, 2, 8]
# for number in numbers:
#     if number % 2 == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")
#

#  creating a clock, and checking the number 5
for num in range(10, -1, -1):  # começa em 10, vai até 0
    if num == 5:
        print(f"{num} Halfway point reached!")
    else:
        print(num)