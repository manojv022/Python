#### generally we have two type progaraming language:
#### 1.) Statically Typed = e.g, C,C++,Java
####                                                   2.) Dynamicallt Typed= e.g, Python


### Why Python is dynamicaly typed language:
Python is considered a dynamically typed language because of how it handles variable types and type checking. Here’s a detailed explanation of dynamic typing in Python:

### What Is Dynamic Typing?

In a dynamically typed language, type checking is done at runtime rather than at compile time. This means that you do not need to explicitly declare the type of a variable when you create it. Instead, the type of a variable is determined by the value it is assigned at runtime.

### Key Characteristics of Dynamic Typing in Python

1. **No Explicit Type Declarations**:
   - In Python, you don’t need to specify the type of a variable when you declare it. For example:
     ```python
     x = 10        # x is an integer
     x = "Hello"   # Now x is a string
     ```
   - The type of `x` changes based on the value assigned to it.

2. **Type Inference at Runtime**:
   - Python infers the type of a variable based on the value it is currently holding. This is done at runtime, allowing for flexible and fluid code.
   - For instance:
     ```python
     def print_value(value):
         print(value)
     
     print_value(123)   # Passing an integer
     print_value("abc") # Passing a string
     ```
   - The function `print_value` can accept arguments of any type because Python determines the type when the function is called.

3. **Flexible Variable Types**:
   - Variables in Python are references to objects, and the type of the object is checked when the variable is used. You can assign different types of values to the same variable.
   - Example:
     ```python
     y = 3.14      # y is a float
     y = [1, 2, 3] # Now y is a list
     ```

4. **Dynamic Type Checking**:
   - Errors related to types are caught at runtime, not at compile time. For example:
     ```python
     a = "Hello"
     b = 5
     result = a + b  # This will raise a TypeError at runtime
     ```
   - Here, Python will raise an error when trying to add a string and an integer, as this operation is invalid.

5. **Type Flexibility in Functions**:
   - Functions in Python can accept arguments of any type, and you don’t need to specify what type of arguments a function expects or returns.
   - Example:
     ```python
     def multiply(a, b):
         return a * b
     
     print(multiply(2, 3))    # Integer multiplication
     print(multiply(2.5, 4))  # Float multiplication
     print(multiply("Hi ", 3)) # String repetition
     ```

### Advantages of Dynamic Typing

1. **Ease of Use**:
   - It simplifies coding because you don’t need to declare types explicitly, making the code more concise and readable.

2. **Flexibility**:
   - It allows for more flexible code since you can write functions and methods that work with various types of data without changing their definitions.

3. **Rapid Prototyping**:
   - Dynamic typing facilitates rapid development and prototyping as you can write and test code quickly without worrying about type constraints.

### Disadvantages of Dynamic Typing

1. **Runtime Errors**:
   - Type errors are caught only at runtime, which can lead to bugs that are harder to detect and debug.

2. **Performance**:
   - Dynamic type checking and type inference can introduce performance overhead compared to statically typed languages, where types are checked at compile time.

### Summary

Python is dynamically typed because:
- It does not require explicit type declarations.
- Variable types are determined at runtime based on the values assigned.
- Type errors are detected only when the code is executed, not before.
- It offers flexibility and ease of use, allowing for rapid development and versatile programming.

This approach to typing contrasts with statically typed languages, where types are checked at compile time and must be explicitly declared.



![image](https://github.com/user-attachments/assets/fce3863a-7ea7-433a-9b72-d8bda02b47d3)

