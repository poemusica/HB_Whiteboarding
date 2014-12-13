
### QUESTIONS from EXERCISE 04 ###

"""
Part 1: Fundamental operations on lists
---------------------------------------

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations:
    * List literals ([], ['hello'], [3, 1, 4, 1, 5, 9], etc.)
    * List indexing (some_list[index])
    * List indexing assignment (some_list[index] = value)
    * List slicing (some_list[start:end])
    * List slicing assignment (some_list[start:end] = another_list)
    * List index deletion (del some_list[index])
    * List slicing deletion (del some_list[start:end])

In this section you will implement functions that each use just one of the
operations. The docstring of each function describes what it should do. Consult
test_list_operations.py for concrete examples of the expected function behavior.
"""

# QUESTION 1
"""Return the first element of the input list."""

# SOLUTION 1
def head(input_list):
    return input_list[0]

# QUESTION 2
"""Return all elements of the input list except the first."""

# SOLUTION 2
def tail(input_list):
    return input_list[1:]

# QUESTION 3
"""Return the last element of the input list."""

# SOLUTION 3
def last(input_list):
    return input_list[-1]

# QUESTION 4
"""Return all elements of the input list except the last."""
def except_last(input_list):
    return input_list[:-1]

# SOLUTION 4
def init(input_list):
    return input_list[0:-1]

# QUESTION 5
"""Return the first three elements of the input list."""
def first_three(input_list):
    return input_list[0:3]

# QUESTION 6
"""Return the last five elements of the input list."""

# SOLUTION 6
def last_five(input_list):
    return input_list[-5:]

# QUESTION 7
"""Return all elements of the input list except the first two and the last two."""

# SOLUTION 7
def middle(input_list):
    return input_list[2:-2]

# QUESTION 8
"""Return the third, fourth, fifth, and sixth elements of the input list.""" 

# SOLUTION 8
def inner_four(input_list):
    return input_list[2:6]

# QUESTION 9
"""Return the sixth, fifth, fourth, and third elements from the end of the
list, in that order.
"""

# SOLUTION 9
def inner_four_end(input_list):
    return input_list[-6:-2]

# QUESTION 10
"""Replace the head of the input list with the value 42."""

# SOLUTION 10
def replace_head(input_list):
    input_list[0] = 42

# QUESTION 11
"""Replace the third and last elements of the input list with the value 37."""

# SOLUTION 11
def replace_third_and_last(input_list):
    input_list[2] = 37
    input_list[-1] = 37

# QUESTION 12
"""Replace all elements of the input list with the the values 42 and 37, in
that order, except for the first two and last two elements.
"""

# SOLUTION 12
def replace_middle(input_list):
    input_list[2:-2] = [42, 37]

# QUESTION 13
"""Remove the third and seventh elements of the input list."""

# SOLUTION 13
def delete_third_and_seventh(input_list):
    del input_list[2:7:4]

# QUESTION 14
"""Remove all elements from the input list except for the first two and the
last two.
"""

# SOLUTION 14
def delete_middle(input_list):
    del input_list[2:-2]

"""
Part 2: Derived operations on lists
-----------------------------------

In this section you will implement your own versions of the standard list methods.
You should use only the primitive operations from Part 1 in your implementations.
For loops are also allowed, such as the following:
    for element in some_list:
        # Do something with element

Each custom method imitates a built-in list method, as described by the docstring
for each function. Play with the built-in methods in the Python REPL to get a feel
for how they work before trying to write your custom version. You may also look at
the test_list_operations.py file for concrete examples of expected behavior.
"""

# QUESTION 1
"""custom_len(input_list) imitates len(input_list)"""

# SOLUTION 1
def custom_len(input_list):
    length = 0
    for item in input_list:
        length += 1
    return length

# QUESTION 2
"""custom_append(input_list, value) imitates input_list.append(value)"""

# SOLUTION 2
def custom_append(input_list, value):
    input_list = input_list + [value]

# QUESTION 3
"""custom_extend(input_list, values) imitates input_list.extend(values)"""

# SOLUTION 3
def custom_extend(input_list, values):
    input_list = input_list + values

# QUESTION 4
"""custom_insert(input_list, index, value) imitates
input_list.insert(index, value)
"""

# SOLUTION 4
def custom_insert(input_list, index, value):
    before = input_list[0:index]
    after = input_list[index:]
    input_list = before + [value] + after

# QUESTION 5
"""custom_remove(input_list, value) imitates input_list.remove(value)"""

# SOLUTION 5
def custom_remove(input_list, value):
    for i in range(len(input_list)):
        if input_list[i] == value:
            del input_list[i]
            return

# QUESTION 6
"""custom_pop(input_list) imitates input_list.pop()"""

# SOLUTION 6
def custom_pop(input_list):
    pass

# QUESTION 7
"""custom_index(input_list, value) imitates input_list.index(value)"""

# SOLUTION 7
def custom_index(input_list, value):
    pass

# QUESTION 8
"""custom_count(input_list, value) imitates input_list.count(value)"""  

# SOLUTION 8
def custom_count(input_list, value):
    pass

# QUESTION 9
"""custom_reverse(input_list) imitates input_list.reverse()"""

# SOLUTION 9
def custom_reverse(input_list):
    pass

# QUESTION 10
"""custom_contains(input_list, value) imitates (value in input_list)"""

# SOLUTION 10
def custom_contains(input_list, value):
    pass

# QUESTION 11
"""custom_equality(some_list, another_list) imitates
(some_list == another_list)
"""

# SOLUTION 11
def custom_equality(some_list, another_list):
    pass
