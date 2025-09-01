from distro import lsb_release_info

# fruits =["peaches", "pears", "apples"]
# years = ["1990", 2.5, 8789, "889"]
#
# print(fruits, years)
#
# # using append method to add, an item in a list
# fruits.append("banana")
# print(fruits)
#
# # using insert method to add an item at a specific index
# fruits.insert(1, "orange")
# print(fruits)
#
# # using extend method to add multiple items at once, in this case we make a union of two lists
# fruits.extend(years)
# print(fruits)
#
# # using remove to remove a item from the list
# fruits.remove("pears")
# print(fruits)
#
# # using pop to remove the last item from the list by position
# fruits.pop(0)
# print(fruits)
#
# # using sort to organize a list
# list_numbers = [155987, 1, 0, 999, 456]
# list_numbers.sort()
# print(list_numbers)
#
# # check a specific item from the list
# print("orange" in fruits)
#
# # count the specific itens from the list
# print(fruits.count("banana"))
#
# # using index to find the position of an item in the list
# print(fruits.index("banana"))

# fruits =["peaches", "pears", "apples"]
# fruits.insert(0, fruits.pop(1))
# print(fruits)

def moving(start_idx:int, steps:int):
    fruits = ["peaches", "pears", "apples", "pineapple", "tomato", "banana"]
    fruit = "fruit"
    move = 0
    idx = start_idx
    print(f"original fruits list{fruits}")
    while move < steps and idx < len(fruits) - 1:
        # for idx in range(10):
        fruits.insert(idx+1, fruits.pop(idx))
        idx += 1
        move += 1
        print(f"The {fruit} is moving", fruits)

moving(0, 5)