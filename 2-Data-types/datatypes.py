"""
1. Numeric types:
   - int: Integer type (e.g., 5, -10).
   - float: Floating-point type (e.g., 3.14, -2.71).
   - complex: Complex number type (e.g., 1+2j).

2. Sequence types:
   - str: String type (e.g., "Hello, World!").
   - list: List type (e.g., [1, 2, 3]).
   - tuple: Tuple type (e.g., (1, 2, 3)).

3. Set types:
   - set: Set type (e.g., {1, 2, 3}).
   - frozenset: Immutable set type (e.g., frozenset({1, 2, 3})).

4. Mapping type:
   - dict: Dictionary type (e.g., {"key": "value", "name": "John"}).

5. Boolean type:
   - bool: Boolean type (True or False).

6. NoneType:
   - None: Represents the absence of a value.

7. Binary types:
   - bytes: Immutable sequence of bytes (e.g., b'hello').
   - bytearray: Mutable sequence of bytes (e.g., bytearray(b'hello')).
   - memoryview: A view of a memory buffer
    that exposes the buffer's content (used in advanced scenarios).
"""

# 1. Numeric types
# 1.1. int
# x = 5
# y = -10
# print('Integer type:', x, y)

# 1.2. float
# x = 3.14
# y = -2.71
# print('float type:', x, y)

# 1.3. complex
# x = 1+2j
# y = -2+3j
# print('complex type:', x, y)


# 2. Sequence types
# 2.1. str
# x = "Hello, World!"
# y = 'Hello, World!'
# print('String type:', x, y)

# 2.2. list
"""
Mutable: Lists are mutable, meaning you can add, remove,
or modify elements after creating the list.

Ordered: Elements in a list are ordered and
can be accessed using their index.

Allows duplicates: Lists can contain duplicate elements.
Syntax: Defined using square brackets [ ].

Example: my_list = [1, 2, 'hello', 3.14]
"""

# x = [1, 2, 3]
# y = [1, 'hello', 3, 2+3j, True, None, ['a', 3.5, 2+3j], (1, 2, 3)]
# print('List type:', x, y)

# 2.3. tuple
"""
Immutable: Unlike lists, tuples are immutable,
meaning once created, you cannot change their elements.

Ordered: Tuples maintain the order of elements
and can be accessed using their index.

Allows duplicates: Tuples can contain duplicate elements.
Syntax: Defined using parentheses ( ).

Example: my_tuple = (10, 'apple', 3.14, 10)
"""
# x = (1, 2, 3)
# y = (1, 'hello', 3, 2+3j, True, None, ['a', 3.5, 2+3j], (1, 2, 3))
# print('Tuple type:', x, y)

# 3.1. Set types
"""
Sets: Mutable, Unordered, No duplicates and
only contain hashable objects and value.

Mutable: Sets are mutable, allowing you to add or remove elements after creation.
Unordered: Sets do not maintain any order for their elements.

No duplicates: Sets do not allow duplicate elements;
each element in a set must be unique.
Syntax: Defined using curly braces { }.

Example: my_set = {1, 2, 3, 3, 4, 5}
(Note that duplicates are removed, and the set becomes {1, 2, 3, 4, 5})

NB: Set can't contain a mutable objects that cannot be hashed.

Hashable objects are those that have a hash value that does not
change during their lifetime and can be used as keys in dictionaries
or elements in sets. Immutable objects like integers, strings,
and tuples are hashable because their values cannot change,
and their hash remains the same.

A list of common mutable objects that cannot be hashed:

Lists: Lists in Python are mutable and cannot be used aselements in sets
or keys in dictionaries because they can change their contents.

Dictionaries: Dictionaries themselves are mutable and cannot be hashed
due to the possibility of changes to their keys or values.

Sets: Sets are mutable collections of unique elements, so they cannot
be used as elements in other sets or keys in dictionaries.

Other Sets: Nested sets (sets containing other sets) are also mutable and,
therefore, unhashable.

Byte Arrays: Byte arrays (mutable sequences of bytes) are unhashable.

User-Defined Objects: If you define your own custom classes and they are
mutable, instances of these classes will also be unhashable.

NB. To check if a certain object is unhashable, you can use the
hash(object) function. If the object is unhashable, this function
will return None.

"""

# Eg. of unhashable error can be raised in one of the following:

# Trying to create a set with a list as an element
# (throws TypeError: unhashable type: 'list')

# my_list = [1, 2, 3]
# try:
#     my_set = {my_list}
#     print(my_set, type(my_set))
# except TypeError as e:
#     print(e)

# resolve TypeError: unhashable type: 'list'
# my_list = [1, 2, 3]
# my_set = set(my_list)
# print(my_set, type(my_set))

# Trying to create a set with another set as an element
# (throws TypeError: unhashable type: 'set')

# nested_set = {1, 2}
# try:
#     my_set = {nested_set}
#     print(my_set, type(my_set))
# except TypeError as e:
#     print(e)

# resolve TypeError: unhashable type: 'set'
# nested_set = {1, 2}
# my_set = set(nested_set)
# print(my_set, type(my_set))

"""
For example, valid elements in a set can include:

Integers: my_set = {1, 2, 3}
Strings: my_set = {'apple', 'banana', 'orange'}
Tuples: my_set = {(1, 2), ('a', 'b', 'c')}
Floats: my_set = {3.14, 2.718}
Booleans: my_set = {True, False}
Sets: my_set = {{1, 2}, {3, 4}}  # (a set containing other sets)

NB: Immutable objects like integers, strings, and tuples are hashable
and can be used in sets and dictionaries. Mutable objects,
on the other hand, are not hashable and cannot be used as keys
or elements in these data structures.

"""

# 3.2. frozenset
"""
frozenset is an immutable version of the set data type in Python.
It behaves like a set, but once created, you cannot modify its elements.
Since frozenset is immutable, it can be used as an element in another
set or as a key in a dictionary. This is because the hash value of a
frozenset remains constant throughout its lifetime, making it hashable.

Proprties of frozenset:

Immutable: Once a frozenset is created, its elements cannot be
modified, added, or removed. It remains constant throughout its lifetime.

Unordered: Like sets, frozenset does not maintain any order for its elements.
It does not support indexing or slicing.

Iterable: You can iterate over the elements of a frozenset
using loops (e.g., for loop).

Hashable: frozenset is hashable, meaning it can be used as an element
in other sets or as a key in dictionaries.

Unique Elements: Like sets, frozenset contains only unique elements.
Any duplicate elements in the input are automatically removed when creating a frozenset.

Set Operations: frozenset supports set operations such as union,
intersection, difference, and symmetric difference.

Creation Syntax: frozenset can be created using the frozenset()
constructor by passing an iterable (e.g., list, tuple, set) as an argument.

"""

# Creating a frozenset
# my_frozenset = frozenset([1, 2, 3, 3, 4])

# Immutable - Attempting to modify a frozenset (Throws an AttributeError)
# my_frozenset.add(5)

# Unordered - Cannot access elements using index or slicing
# print(my_frozenset[0])  # Throws a TypeError

# Iterable - Can be iterated over using loops
# for item in my_frozenset:
#     print(item)

# Hashable - Can be used as an element in a set
# my_set = {my_frozenset}

# Unique Elements - Duplicates are automatically removed during creation
# print(my_frozenset)  # Output: frozenset({1, 2, 3, 4})

# Set Operations
# set1 = frozenset([1, 2, 3])
# set2 = frozenset([3, 4, 5])
# union_set = set1.union(set2)
# print(union_set)  # Output: frozenset({1, 2, 3, 4, 5})

# 4.1. Mapping types: dict
"""
Dictionary: A dictionary is a collection of key-value pairs.
A key is used to reference a value in the dictionary.

Properties of a dictionary:

Mutable: Dictionaries are mutable, meaning you can add, remove,
or modify key-value pairs after creating the dictionary.

Unordered: Dictionaries do not maintain any order for their elements.
From Python 3.7 onwards, dictionaries also preserve insertion order.

Key-Value Pairs: Elements in a dictionary are stored as key-value pairs.
Each key is associated with a corresponding value.

Keys must be unique and hashable: Each key in the dictionary
must be unique, and it must be hashable. Hashable keys enable
efficient retrieval and storage of key-value pairs.

Values can be duplicated: Dictionary values can be duplicated,
i.e., multiple keys can map to the same value.

Dynamic Size: Dictionaries can dynamically grow or shrink
as elements are added or removed.

Accessing Elements: You can access dictionary elements using their keys.

Membership Test: You can check if a key exists
in a dictionary using the in keyword.

Methods: Dictionaries have various built-in methods for manipulating
and retrieving data, such as keys(), values(), items(), get(), pop(), etc.

"""

# Creating a dictionary
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Mutable - Adding a new key-value pair
# my_dict['occupation'] = 'Engineer'

# Output: {'name': 'John', 'age': 30, 'city': 'New York',
# 'occupation': 'Engineer'}

# print(my_dict)

# Unordered - Elements are not guaranteed to be in any
# specific order (since Python 3.7, insertion order is preserved)
# Output: {'name': 'John', 'age': 30, 'city': 'New York',
# 'occupation': 'Engineer'}

# print(my_dict)

# Key-Value Pairs
# print(my_dict['name'])  # Output: 'John'
# print(my_dict['age'])   # Output: 30

# Keys must be unique and hashable
# my_dict = {1: 'One', 2: 'Two', 3: 'Three'}
# my_dict = {[1, 2]: 'list'}  # This would raise a TypeError
# since lists are unhashable

# Values can be duplicated
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York',
#            'gender': 'Male', 'occupation': 'Engineer'}

# Accessing Elements - Using keys
# print(my_dict['name'])  # Output: 'John'
# print(my_dict['gender'])  # Output: 'Male'

# Membership Test
# print('name' in my_dict)  # Output: True
# print('country' in my_dict)  # Output: False

# Methods
# keys = my_dict.keys()
# values = my_dict.values()
# items = my_dict.items()

# Output: dict_keys(['name', 'age', 'city', 'gender', 'occupation'])
# print(keys)
# Output: dict_values(['John', 30, 'New York', 'Male', 'Engineer'])
# print(values)
# Output: dict_items([('name', 'John'), ('age', 30),
# ('city', 'New York'), ('gender', 'Male'), ('occupation', 'Engineer')])
# print(items)

# 5.1. Boolean type:
"""
Two Values: Boolean type represents only two possible values:
True and False.

Case-Sensitive: The values True and False must be capitalized,
i.e., True, not true, and False, not false.

Used for Logic: Booleans are primarily used for logical operations
and comparisons.

Result of Comparisons: Comparisons in Python (e.g., ==, !=, <, >, <=, >=)
return Boolean values (True or False).

Result of Logical Operations: Logical operations like and, or, and
not also return Boolean values.

Numeric Conversion: Booleans can be implicitly converted to integers
(True as 1, False as 0) and vice versa.

Subclass of Integers: In Python, True is a subclass of int with a value
of 1, and False is a subclass of int with a value of 0.

Truthy and Falsy: In Boolean contexts, some values other than True
and False are considered "truthy" or "falsy," meaning they evaluate
to True or False, respectively.

"""

# Booleans have two values: True and False
# a = True
# b = False

# Comparisons return Boolean values
# result1 = 10 > 5  # result1 is True
# result2 = 7 == 7  # result2 is True
# result3 = 3 < 1   # result3 is False

# Logical operations return Boolean values
# result4 = True and False  # result4 is False
# result5 = True or False   # result5 is True
# result6 = not True        # result6 is False

# Implicit conversion to integers
# value1 = int(True)  # value1 is 1
# value2 = int(False)  # value2 is 0

# Truthy and Falsy values
# value3 = bool(0)      # value3 is False
# value4 = bool(42)     # value4 is True
# value5 = bool("")     # value5 is False
# value6 = bool("Hello")  # value6 is True
# value7 = bool([])     # value7 is False
# value8 = bool([1, 2])  # value8 is True


# 6.1. None type
"""
The NoneType is a data type in Python that represents a single value,
None. It is used to indicate the absence of a value or a null value.

Here are the properties of the NoneType:

Single Value: The NoneType has only one possible value, which is None.

Represents Absence: It is used to denote the absence of a value or the
result of a function that doesn't explicitly return anything.

Similar to Null: In many programming languages,
None is analogous to null or nil values.

Falsy Value: In Boolean contexts, None is considered a "falsy" value,
meaning it evaluates to False.

Special Object: None is a special singleton object in Python, and
there can only be one instance of it in any given Python interpreter session.

Comparison: You should use is or is not when comparing with None.
Using == or != for comparison may lead to unexpected
results due to the way None is implemented.

"""

# None is the absence of a value
# my_variable = None

# Singleton - All references to None point to the same object
# var1 = None
# var2 = None
# print(var1 is var2)  # Output: True

# Non-Callable
# None()  # This would raise a TypeError:
# 'NoneType' object is not callable

# Comparison
# result1 = None == None      # result1 is True
# result2 = None != "Hello"   # result2 is True
# result3 = None == False     # result3 is False

# Return Value - Functions with no explicit return
# value return None by default


# def my_function():
#     print("Hello")


# result4 = my_function()  # Output: "Hello"
# print(result4)           # Output: None

# Default Value - Unassigned variables or function
# parameters are initialized to None


# def my_function2(parameter=None):
#     print(parameter)


# my_function2()  # Output: None

# # Boolean Evaluation - None is considered "falsy"
# if not None:
#     print("None is falsy")  # Output: "None is falsy"


# 7.1. Binary type
"""
In Python, binary types refer to data types that represent
sequences of bytes or binary data. The two main binary types in Python are:

bytes Type:

Immutable: bytes objects are immutable, meaning you cannot modify their
contents after creation.

Sequence of Bytes: bytes objects represent a sequence of bytes
(8-bit values) and are used to store binary data.

Literal Syntax: bytes objects can be created using a literal syntax
with a b prefix and escape sequences (e.g., b'hello').

Bytes Literal: The elements of a bytes object are integers in the
range of 0 to 255 (representing ASCII values).

bytearray Type:

Mutable: Unlike bytes, bytearray objects are mutable, allowing you
to modify their contents after creation.

Sequence of Bytes: bytearray objects also represent a sequence of bytes,
similar to bytes.

Literal Syntax: bytearray objects can be created using a literal syntax
with a bytearray() constructor and escape sequences
(e.g., bytearray(b'hello')).

Bytes Literal: The elements of a bytearray object are
integers in the range of 0 to 255.

"""

# # bytes type
# my_bytes = b'hello'
# print(type(my_bytes))  # Output: <class 'bytes'>
# print(my_bytes)        # Output: b'hello'

# # Immutable - Cannot modify bytes after creation
# # my_bytes[0] = 72  # This would raise a TypeError

# # Sequence of Bytes
# for byte in my_bytes:
#     # Output: 104, 101, 108, 108, 111 (ASCII values for 'h', 'e', 'l', 'l', 'o')
#     print(byte)

# # bytearray type
# my_bytearray = bytearray(b'hello')
# print(type(my_bytearray))  # Output: <class 'bytearray'>
# print(my_bytearray)        # Output: bytearray(b'hello')

# # Mutable - Can modify bytearray after creation
# my_bytearray[0] = 72  # Change 'h' to 'H'
# print(my_bytearray)   # Output: bytearray(b'Hello')

# # Sequence of Bytes
# for byte in my_bytearray:
#     # Output: 72, 101, 108, 108, 111 (ASCII values for 'H', 'e', 'l', 'l', 'o')
#     print(byte)
