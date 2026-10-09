# # variables and data types

# a = 10  # integer
# b = 3.14  # float
# c = "Hello, World!"  # string

# my_list = [1, 2, 3, 4, 5]  # list
# my_tuple = (1, 2, 3)  # tuple
# my_set = {1, 2, 3, 3}  # set
# my_tuple = (1, 2, 3, 4)  # tuple
# print(my_set)  # Output: {1, 2, 3} (duplicates are removed)
# print(my_tuple)  # Output: (1, 2, 3, 4)
# my_dict = {"name": "Alice", "age": 30}  # dictionary
# print(my_dict)  # Output: {'name': 'Alice', 'age': 30}


# # operators

# # arithmetic operators
# x = 10
# y = 3
# print(x + y)  # addition, Output: 13
# print(x - y)  # subtraction, Output: 7
# print(x * y)  # multiplication, Output: 30
# print(x / y)  # division, Output: 3.333333333333333
# print(x // y)  # floor division, Output: 3
# print(x % y)  # modulus, Output: 1

# # comparison operators
# print(x == y)  # equal to, Output: False
# print(x != y)  # not equal to, Output: True
# print(x > y)  # greater than, Output: True
# print(x < y)  # less than, Output: False
# print(x >= y)  # greater than or equal to, Output: True
# print(x <= y)  # less than or equal to, Output: False

# # logical operators
# print(x > 5 and y < 5)  # logical AND, Output: True
# print(x > 5 or y < 5)  # logical OR, Output: True
# print(not(x > 5))  # logical NOT, Output: False

# # assignment operators
# x += 5  # equivalent to x = x + 5
# print(x)  # Output: 

# # ternary operator
# age = 20
# status = "Adult" if age >= 18 else "Minor"
# print(status)  # Output: Adult

# # bitwise operators
# x = 5  # binary: 0101
# y = 3  # binary: 0011
# print(x & y)  # bitwise AND, Output: 1 (binary: 0001)
# print(x | y)  # bitwise OR, Output: 7 (binary: 0111)
# print(x ^ y)  # bitwise XOR, Output: 6 (binary: 0110)
# print(~x)  # bitwise NOT, Output: -6 (binary: 1010)
# print(x << 1)  # left shift, Output: 10 (binary: 1010)
# print(x >> 1)  # right shift, Output: 2 (binary: 0010)


# # control flow statements

# # if-else statement
# x = 10
# if x > 0:
#     print("x is positive")
# else:
#     print("x is non-positive")

# # if-elif-else statement
# x = 0
# if x > 0:
#     print("x is positive")
# elif x == 0:
#     print("x is zero")
# else:
#     print("x is negative")

# # case statement (using match-case in Python 3.10+)
# x = 2
# match x:
#     case _ if x % 2 == 0:
#         print("x is even")
#     case 1:
#         print("x is one")
#     case 2:
#         print("x is two")
#     case 3:
#         print("x is three")
#     # when x is even

# # for loop
# for i in range(5):
#     print(i)  # Output: 0, 1, 2, 3, 4

# # for loop with hops
# for i in range(0, 10, 2):
#     print(i)  # Output: 0, 2, 4, 6, 8

# # reversal for loop
# for i in range(5, 0, -1):
#     print(i)  # Output: 5, 4, 3, 2, 1

# # while loop
# count = 0
# while count < 5:
#     print(count)  # Output: 0, 1, 2, 3, 4
#     count += 1

# def greet(name):
#     return f"Hello, {name}!"


dict = {"name": "Alice", "age": 30, "city": "New York"}
[(key, value) for key, value in dict.items()]


def scale_feature (sample:dict, bounds:dict) -> dict:
    scaled_sample = {}
    for i,j in sample.items():
        if i in bounds:
            min_bound, max_bound = bounds[i]
            scaled_sample[i] = (j - min_bound) / (max_bound - min_bound)
    return scaled_sample

print(scale_feature({"feature1": 5, "feature2": 10}, {"feature1": (0, 10), "feature2": (0, 20)}))  # Output: {'feature1': 0.5, 'feature2': 0.5}

# lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25
