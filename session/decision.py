# 🌟 Decision Making (if, elif, else) 🤔

# if: Executes a block of code if the condition is True.
# elif: Executes a block of code if the previous if condition is False and the elif condition is True. You can have multiple elif blocks.
# else: Executes a block of code if none of the previous if or elif conditions are True.


#🌟 While Loop 💀⚡💀⚡

# Repeats a block of code as long as a given condition is True.
# The condition is checked before each iteration.

#🌟 For Loop 😵‍💫😵‍💫

# Iterates over a sequence (e.g., a list, tuple, string, or range).
# Executes the code block for each item in the sequence.


#🌟 Continue Statement

# Skips the remaining part of the current iteration of the loop and proceeds to the next iteration.

#🌟Pass Statement

# Acts as a placeholder. It does nothing, but it's necessary to maintain the proper structure of the code.

#🌟Break Statement

# Exits the loop immediately, regardless of whether the loop condition is still True.


#------------😎-----------😎-----------😎-----------😎-----------😎-----------😎-----------😎-----------😎


# Decision Making (if, elif, else)

age = 25

if age < 18:
    print("You are a minor.")
elif 18 <= age < 65:  # Corrected the elif condition
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# While Loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# For Loop
for i in range(5):
    print("Iteration:", i)

# Continue Statement
for i in range(5):
    if i == 2:
        continue  # Skip the rest of the current iteration
    print("Iteration:", i)

# Pass Statement (used as a placeholder)
for i in range(5):
    if i == 2:
        pass  # Do nothing
    else:
        print("Iteration:", i)

# Break Statement
for i in range(5):
    if i == 3:
        break  # Exit the loop immediately
    print("Iteration:", i)

