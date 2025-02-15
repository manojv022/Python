# Good Practices for Creating Variables in Python

# 1. Use descriptive names
#   a) Meaningful names improve code readability
age = 30 
user_name = "Ramdev Baba"
product_price = 9.99

# 2. Follow conventions (PEP 8)
#   a) Snake case for variables (lowercase with underscores)
first_name = "Alice" 
last_name = "Wonderland"

# 3. Avoid reserved keywords
#   a) Do not use Python keywords as variable names (e.g., 'if', 'for', 'while', 'class', 'def')
#   b) Example:
#      if = 10  # Incorrect - 'if' is a keyword

# 4. Be consistent
#   a) Maintain consistent naming conventions throughout your code.

# 5. Use constants appropriately
#   a) For values that should not change, use uppercase letters with underscores
MAX_ATTEMPTS = 3
PI = 3.14159

# 6. Consider data types
#   a) Choose appropriate data types for variables 
#      (e.g., use integers for whole numbers, floats for decimal numbers)

# Example:
customer_id = 123  # Integer
customer_name = "John Smith"  # String
is_active = True  # Boolean

# 7. Avoid single-letter variable names (except for short loop variables)
#   a) Use meaningful names instead of single letters (unless the variable's scope is very limited)
#      for i in range(10):  # 'i' is acceptable in this context

# 8. Initialize variables before use
#   a) Always initialize variables with a value before using them

# Example:
count = 0  # Initialize count to 0

# 9. Use meaningful variable names within functions
#   a) Choose names that reflect the purpose of the variable within the function's context


#------------😎-----------😎-----------😎-----------😎-----------😎-----------😎-----------😎-----------😎


# # This Python code demonstrates various data types and operators.

# # 1. Numbers
# #   a) Integers
# integer_value = 10
# print("Integer:", integer_value, type(integer_value)) 

# #   b) Floats
# float_value = 3.14
# print("Float:", float_value, type(float_value))

# #   c) Complex Numbers
# complex_value = 2 + 3j
# print("Complex:", complex_value, type(complex_value))

# # 2. Strings
# string_value = "Hello, World!"
# print("String:", string_value, type(string_value))

# # 3. Boolean
# boolean_true = True
# boolean_false = False
# print("Boolean (True):", boolean_true, type(boolean_true))
# print("Boolean (False):", boolean_false, type(boolean_false))

# # 4. Lists
# list_value = [1, 2, 3, "apple", True]
# print("List:", list_value, type(list_value))

# # 5. Tuples
# tuple_value = (10, 20, 30)
# print("Tuple:", tuple_value, type(tuple_value))

# # 6. Sets
# set_value = {1, 2, 2, 3}  # Sets automatically remove duplicates
# print("Set:", set_value, type(set_value))

# # 7. Dictionaries
# dictionary_value = {"name": "Alice", "age": 30, "city": "New York"}
# print("Dictionary:", dictionary_value, type(dictionary_value))

# # Arithmetic Operators
# print("\nArithmetic Operators:")
# num1 = 10
# num2 = 5
# print("Addition:", num1 + num2)
# print("Subtraction:", num1 - num2)
# print("Multiplication:", num1 * num2)
# print("Division:", num1 / num2)
# print("Floor Division:", num1 // num2)
# print("Modulus:", num1 % num2)
# print("Exponentiation:", num1 ** 2)

# # Comparison Operators
# print("\nComparison Operators:")
# print("Equal to:", num1 == num2)
# print("Not Equal to:", num1 != num2)
# print("Greater Than:", num1 > num2)
# print("Less Than:", num1 < num2)
# print("Greater Than or Equal To:", num1 >= num2)
# print("Less Than or Equal To:", num1 <= num2)

# # Logical Operators
# print("\nLogical Operators:")
# print("and:", True and True)
# print("or:", True or False)
# print("not:", not True)

# # Bitwise Operators (for integers)
# print("\nBitwise Operators:")
# num3 = 10  # Binary: 1010
# num4 = 5   # Binary: 0101
# print("Bitwise AND:", num3 & num4)
# print("Bitwise OR:", num3 | num4)
# print("Bitwise XOR:", num3 ^ num4)
# print("Left Shift:", num3 << 1)  # Shift bits to the left by 1
# print("Right Shift:", num3 >> 1)  # Shift bits to the right by 1

# # Membership Operators
# print("\nMembership Operators:")
# list_values = [1, 2, 3]
# print("in:", 2 in list_values)
# print("not in:", 4 not in list_values)

# # Identity Operators
# print("\nIdentity Operators:")
# a = 10
# b = 10
# c = 20
# print("is:", a is b)  # Checks if both objects refer to the same memory location
# print("is not:", a is not c)
