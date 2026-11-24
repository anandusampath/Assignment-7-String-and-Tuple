"""
Python Assignment 1: Data Structures - Strings & Tuples
"""

# =====================================================
# STRINGS
# =====================================================

# ----- 1. String Concatenation -----
print("=" * 50)
print("1. STRING CONCATENATION")
print("=" * 50)

string1 = "Hello "
string2 = input("Enter your Name: ")
greeting = string1 + string2
print(greeting)

string3 = ", welcome to Python programming"
greeting = greeting + string3
print(greeting)

# ----- 2. String Slicing and Indexing -----
print()
print("=" * 50)
print("2. STRING SLICING AND INDEXING")
print("=" * 50)

text = greeting  # concatenated string from Question 1

# a. First character
print("a. First character:", text[0])

# b. Last character
print("b. Last character:", text[-1])

# c. First 5 characters
print("c. First 5 characters:", text[:5])

# d. Last 11 characters
print("d. Last 11 characters:", text[-11:])

# e. String in reverse
print("e. Reversed string:", text[::-1])

# f. Print the word "Python" using slicing
start = text.index("Python")
end = start + len("Python")
print("f. Word 'Python':", text[start:end])

# ----- 3. String Methods -----
print()
print("=" * 50)
print("3. STRING METHODS")
print("=" * 50)

strM = "Python beginner tutorial"
print("Original string:", strM)

# a. Uppercase
print("a. Uppercase:", strM.upper())

# b. Lowercase
lower_str = strM.lower()
print("b. Lowercase:", lower_str)

# c. Capitalize -> returns the sentence to its original form
print("c. Capitalize:", lower_str.capitalize())

# d. Count occurrences of 't'
print("d. Occurrences of 't':", strM.count("t"))

# e. Replace "Python" with "Machine Learning"
print("e. After replace:", strM.replace("Python", "Machine Learning"))

# =====================================================
# TUPLES
# =====================================================
print()
print("=" * 50)
print("TUPLES")
print("=" * 50)

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
print("1st tuple:", tuple1)
print("2nd tuple:", tuple2)

# a. Concatenate the two tuples
t_combine = tuple1 + tuple2
print("a. t_combine:", t_combine)

# b. Repeat the elements of t_combine 3 times
print("b. t_combine repeated 3 times:", t_combine * 3)

# c. Access the 3rd element
print("c. 3rd element:", t_combine[2])

# d. Access the first three elements
print("d. First three elements:", t_combine[:3])

# e. Access the last three elements
print("e. Last three elements:", t_combine[-3:])
