stuff = {"food": 15, "energy": 100, "enemies": 3}
# print a specific item for the dictionary
print(stuff.get("food"))
# print all items from the dictionary
print(stuff.items())

# print all keys from the dictionary
print(stuff.keys())

# using popitem to remove item from the list
# print(stuff.popitem())

# using default to define a default value for a key
stuff.setdefault("food")
print(stuff)
# add a new key with a default value
stuff.setdefault("friends", 123)
print(stuff)

# using update to add a new key with a value or only update a key:value
stuff.update({"team": 20, "league": 456})
print(stuff)
stuff.update({"team": 300, "league": 6})
print(stuff)
# another using update to change a key value
stuff.update(food = 123)
print(stuff)
