
from decimal import Decimal
import math

#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

my_list= ["Python","Java","Ruby","Go","Swift"]

my_tuple = ("Python", "Guido van Rossum", "1991")

my_float = 17.25

my_integer = 100

my_decimal = Decimal(3.75)

my_dictionary = {
    "language" : "kotlin",
    "year": 2011,
    "creator": "JetBrains",
    "type": "compilado",
    "paradigm": "multiparadigma",
    "popular_use": "apps Android",
    "extension": ".kt",
    "frameworks": ["Ktor", "Spring"]
}

print(type(my_list))
print(type(my_tuple))
print(type(my_float))
print(type(my_integer))
print(type(my_decimal))
print(type(my_dictionary))

# Exercise 2: Round your float up.

print(math.ceil(my_float))


# Exercise 3: Get the square root of your float.

print(math.sqrt(my_float))

# Exercise 4: Select the first element from your dictionary.

first_element = my_dictionary.items()
print(list(first_element)[0])

# Exercise 5: Select the second element from your tuple.

print(my_tuple[1])


# Exercise 6: Add an element to the end of your list.

my_list.append("JavaScript")
print(my_list)

# Exercise 7: Replace the first element in your list.

my_list.insert(0,"kotlin")
print(my_list)

# Exercise 8: Sort your list alphabetically.

my_list.sort()
print(my_list)

# Exercise 9: Use reassignment to add an element to your tuple.

my_tuple += ("multiparadigma",)
print(my_tuple)
