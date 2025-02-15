# Modules / libraries

#import statment
from sabji import aloo as a
from sabji import gajar as g


#print(g,a)


import math as m


#print(m.sqrt(49))


#---------chempy------------


# # importing the module
# from chempy.util import periodic

# # number of elements to be fetched
# n = 20

# # displaying the information
# print("Atomic No.\tName\t\tSymbol\t\tMass")

# # fetching the information for
# # the first 10 elements
# for i in range(1, n + 1):

# 	# displaying the atomic number
# 	print(i, end = "\t\t")

# 	# displaying the name
# 	if len(periodic.names[i]) > 7:
# 		print(periodic.names[i], end = "\t")
# 	else:
# 		print(periodic.names[i], end = "\t\t")

# 	# displaying the symbol
# 	print(periodic.symbols[i], end = "\t\t")

# 	# displaying the mass
# 	print(periodic.relative_atomic_masses[i])


#------------------ OS module ----------------

# import os

# # Define the file path
# file_name = "mango.txt"  #keep a file ready for this

# # Use os.path to construct the full path (if needed)
# file_path = os.path.join(os.getcwd(), file_name)

# # Check if the file exists
# if os.path.exists(file_path):
#     print(f"File '{file_name}' exists at: {file_path}")

#     # Open and read the file
#     with open(file_path, "r") as file:
#         content = file.read()
#         print("File Content:")
#         print(content)
# else:
#     print(f"File '{file_name}' does not exist at 🧐: {file_path}")


# import os

# val = os.path.exists("C:\cloud1\mango.txt")

# print(val)

# import time
# print(time.time())


# import time

# curr = time.time()
# print("Current time in seconds since epoch =", curr)

# # Convert to a human-readable format
# readable_time = time.ctime(curr)
# print("Human-readable time =", readable_time)



# good example

# import time as t

# t1 = t.time()
# for i in range(1000):
#     print("Paratha","🌶️🌶️")

# t2 = t.time()

# print(f'It took {t2-t1} seconds to make this Parathas')


# 100 parathas = 0.006999492645263672 secs

# 1000 parathas = 0.07454156875610352


# import numpy as np

# l = [0,1,2,3,4,5,6,7,8,9]

# a = np.array(l)

# print(f' THis is a list {l}')

# print(f' THis is an array {a}')



import sys
import numpy as np

# Create a Python list
python_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a NumPy array with the same elements
numpy_array = np.array(python_list)

# Get the size of the Python list
list_size = sys.getsizeof(python_list)

# Get the size of the NumPy array
array_size = numpy_array.nbytes

# Print the sizes
print(f"Size of Python list: {list_size} bytes")
print(f"Size of NumPy array: {array_size} bytes")

# Compare the sizes
if list_size < array_size:
    print("Python list uses less memory.")
elif list_size > array_size:
    print("NumPy array uses less memory.")
else:
    print("Both have the same memory usage.")


print(python_list)
print(numpy_array)
