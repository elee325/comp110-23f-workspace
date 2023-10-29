"""Practice with Dictionaries."""

# Constructing a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

# updating number of orders of vanilla, adjusting the value
ice_cream["vanilla"] = 10
# ice_cream["vanilla"] += 2

# Adding a key, value pair to a dictionary
ice_cream["mint"] = 3

# Removing a key, value pair from a dictionary
ice_cream.pop("mint")

print("Made my dictionary.")
print(ice_cream)

# Printing how many orders of chocolate by accessing a value
print(f"There are {ice_cream['chocolate']} orders of chocolate")

# Getting the length
print(f"The number of key value pairs: {len(ice_cream)}")

# checking if key is in dictionary
print("Is mint in ice_cream?")
print("mint" in ice_cream)
print("Is chocolate in ice_cream?")
print("chocolate" in ice_cream)

# using it in a conditional
if "mint" in ice_cream == True:
    print(f"There are {ice_cream['mint']} orders of mint.")
else: 
    print("no orders of mint")

for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders")