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
temp_f = 40
while temp_f > 32:
    print(f"Thw water is {temp_f} degress")
    temp_f -= 1
    if temp_f == 33:
        break

# using continue in a loop for
for i in range(1,11):
    if i == 7:
        print("we skipped 7")
        continue
    print(f"this is the number {i}")

# using pass in a loop for
for i in range(1,11):
    if i == 3:
        pass
    else:
        print(f"this is the number {i}")