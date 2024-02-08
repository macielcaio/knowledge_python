###  Finally  ###


# try:
#    print("Hello")
#    print(1 / 0)
# except ZeroDivisionError:
#    print("Divided by zero")
# finally:
#    print("This code will run no matter what")

# try:
#     print(1)
# except:
#     print(2)
# finally:
#     print(3)

# try:
#    print(1)
# except ZeroDivisionError:
#    print(2)
# else:
#    print(3)

# try:
#    print(1/0)
# except ZeroDivisionError:
#    print(4)
# else:
#    print(5)

try:
    print(1)
    print(1 + "1" == 2)
    print(2)
except TypeError:
    print(3)
else:
    print(4)