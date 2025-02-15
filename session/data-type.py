"""Numbers, Strings, Lists, Tuples, Sets, Dictionary
Examples: WAC for understanding List vs Tuple
Example: WAC to print pattern """

# Numbers
# Integers
integer_number = 10
print(f"Integer: {integer_number}")

# Floating-point numbers
float_number = 3.14
print(f"Float: {float_number}")

# Strings
string_value = "Hello, World!"
print(f"String: {string_value}")

# Lists (Mutable)
my_list = [1, 2, 3, "apple", "banana"]
print(f"List: {my_list}")
my_list.append(4)  # Modifying the list
print(f"Modified List: {my_list}")

# Tuples (Immutable)
my_tuple = (1, 2, 3, "apple", "banana")
print(f"Tuple: {my_tuple}")
# my_tuple.append(4)  # This will raise an error as tuples are immutable

# Sets (Unordered, Unique elements)
my_set = {1, 2, 2, 3, "apple"}  # Duplicates are removed
print(f"Set: {my_set}")

# Dictionaries (Key-value pairs)
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Dictionary: {my_dict}")
print(f"Name: {my_dict['name']}")

# WAC for understanding List vs Tuple
print("\nWAC: List vs Tuple")
print("Lists are mutable, meaning you can change their elements after creation.")
print("Tuples are immutable, meaning you cannot change their elements after creation.")
print("Use lists when you need to frequently add, remove, or modify elements.")
print("Use tuples when you need to ensure that the data remains constant.")

# WAC to print pattern
print("\nWAC: Print Pattern (Pyramid)")

rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()



    #simple triangle

    rows = 5
for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print()




####----------------Turtle

import turtle 
skk = turtle.Turtle() 

for i in range(100): 
	skk.forward(20) 
	skk.right(10) 
	
for i in range(100): 
	skk.forward(20) 
	skk.left(10) 
