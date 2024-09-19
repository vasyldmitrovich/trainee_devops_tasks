import constants

print("Start learning data types")

bool_var = True
int_var = 12
float_var = 12.5
list_var = ['abcd', 786, 2.23, 'john', 70.2]
tuple_var = ('abcd', 786, 2.23, 'john', 70.2)
str_var = "My name is ..."
set_var = {'w', 'q', 'r', 't', 'w', 'y'}
frozenset_var = frozenset('qwerty')
dict_var = {'name': 'john', 'id': 6734, 'role': 'admin'}

print("bool_var: ", bool_var, " \tint_var: ", int_var, " \tfloat_var: ", float_var,
      " \nlist_var: ", list_var, " \ntuble_var: ", tuple_var,
      " \n set_var {'w', 'q', 'r', 't', 'w', 'y'}: ", set_var,
      " \nstr_var: ", str_var, " \nfrozenset_var: ", frozenset_var,
      " \ndict_var: ", dict_var, "\n")

print("Id immutable variable 'int_var' before changing: ", id(int_var))
int_var = 132
print("Id immutable variable 'int_var' after changing: ", id(int_var), "\n")
print("Id mutable variable 'list_var' before changing: ", id(list_var), f"\n {list_var}")
list_var.append('bla')
print("Id mutable variable 'list_var' after changing: ", id(list_var), f"\n {list_var}", "\n-----")

a = 10
b = a
print("If a=10 and b = a")
print(f"a: {a}: id: ", id(a), f"b: {b}: id: ", id(b))
b += 1
print(f"a: {a}: id: ", id(a), f"b: {b}: id: ", id(b))
a += 1
print(f"a: {a}: id: ", id(a), f"b: {b}: id: ", id(b))
print(
    "Because a number between -5 and 256 is cached by Python to optimize memory, so all variables assigned these values refer to the same object in memory.\n")

d = 1000
k = d + 1
print("If d=1000 and k = d+1")
print(f"d: {d}: id: ", id(d), f"k: {k}: id: ", id(k))
d += 1
print("If d+=1 ")
print(f"d: {d}: id: ", id(d), f"k: {k}: id: ", id(k))
print(
    "Numbers bigger than 256 do not cached each time a new value is assigned, a new object is created in memory with a new ID.\n-----")

x = 1.0
y = x
print("If x = 1.0 and y = x")
print(f"x: {x}, id: {id(x)}, y: {y}, id: {id(y)}")
y += 1.0
print("If x = 1.0 and y += 1.0")
print(f"x: {x}, id: {id(x)}, y: {y}, id: {id(y)}")
print(
    "Fractional numbers are not cached like some integers, so every time a new float value is created, a new object is created in memory.\n-----")

list1 = [1, 2, 3]
list2 = list1
print("If list1 = [1, 2, 3] and list2 = list1")
print(f"list1: {list1}, id: {id(list1)}, list2: {list2}, id: {id(list2)}")
list2.append(4)
print("list2.append(4)")
print(f"list1: {list1}, id: {id(list1)}, list2: {list2}, id: {id(list2)}")
print(
    "Lists are mutable, and when you assign a list to another variable, both variables refer to the same object in memory.\n-----")

tuple1 = (1, 2, 3)
tuple2 = tuple1
print("If tuple1 = (1, 2, 3) and tuple2 = tuple1")
print(f"tuple1: {tuple1}, id: {id(tuple1)}, tuple2: {tuple2}, id: {id(tuple2)}")
tuple2 = tuple2 + (4,)
print("tuple2 = tuple2 + (4,)")
print(f"tuple1: {tuple1}, id: {id(tuple1)}, tuple2: {tuple2}, id: {id(tuple2)}")
print("Tuples are immutable, so a new tuple is created every time its contents change.\n-----")

str1 = "hello"
str2 = str1
print("If str1 = hello and str2 = str1")
print(f"str1: {str1}, id: {id(str1)}, str2: {str2}, id: {id(str2)}")
str2 += " world"
print("str2 += world")
print(f"str1: {str1}, id: {id(str1)}, str2: {str2}, id: {id(str2)}")
print("Strings are immutable. Short strings can be cached, as can small integers.\n-----")

set1 = {1, 2, 3}
set2 = set1
print("If set1 = {1, 2, 3} and set2 = set1")
print(f"set1: {set1}, id: {id(set1)}, set2: {set2}, id: {id(set2)}")
set2.add(4)
print("set2.add(4)")
print(f"set1: {set1}, id: {id(set1)}, set2: {set2}, id: {id(set2)}")
print("Sets are mutable, so a new set is created each time its contents change.\n-----")

dict1 = {'a': 1, 'b': 2}
dict2 = dict1
print("If dict1 = {'a': 1, 'b': 2} and dict2 = dict1")
print(f"dict1: {dict1}, id: {id(dict1)}, dict2: {dict2}, id: {id(dict2)}")
dict2['c'] = 3
print("dict2['c'] = 3")
print(f"dict1: {dict1}, id: {id(dict1)}, dict2: {dict2}, id: {id(dict2)}")
print("Dictionaries are mutable, so a new dictionary is created every time its contents change.\n----\n-")

'''
Small integers and short strings can be cached, so variables assigned to these values can have the same identifiers.
Fractional numbers, tuples, lists, sets, and dictionaries are not cached in this way, 
and each time a new value or object is created, a new ID is created.
Variable data types (lists, sets, dictionaries) retain their identifier when their contents change, 
if they are changed through object methods. But if a new object is assigned to a variable, the identifier changes.
'''

type_is = type(dict2) is dict
print("Variable 'dict2' is or not type disc: ", type_is, "\n-----")

z = 1 + 2 + 3 + \
    4
print(f"z is: {z}")
z = (1 + 2 + 3 + 4 + 5)
type_z = type(z)
print(f"z = (1 + 2 + 3 + 4 + 5) is: {z}", type_z)
z = [1 + 2 + 3 + 4 + 5 + 6]
type_z = type(z)
print(f"z = [ 1 + 2 + 3 + 4 + 5 + 6] is: {z}", type_z)
z = {1 + 2 + 3 + 4 + 5 + 4 + 3, 23, 22}
type_z = type(z)
print("z = { 1 + 2 + 3 + 4 + 5 + 4 + 3, 23, 22} is: ", z, type_z, "\n-----")

# Cycle
print("Cycle from 1 to 4, if == 2 break")
for i in range(1, 4):
    print(i)
    if i == 2:
        break

if True: print('if True: print Hello In one line'); a = 3  # In one line

if True:
    print('if True print and set a=5')
    a = 5
    print(a)

x = y = z = 1
print("x = y = z = 1", "z: ", z, " y: ", y, " x: ", x)
print("PI from file constants.PI is: ", constants.PI)
PI = 3.14
PI += 1
print("Create var PI and set new value, PI: ", PI)
PI = 2.15
print("PI: ", PI, f"variable PI from file constants.PI: {constants.PI}", f", and from class, constants.Constants.PI: ",
      constants.Constants.PI)

x = 3.14j
print("Complex literal: ", x)
val1 = None
val2 = 2
print("With val1 = None and val2=2:", val1, val2, "\n---\n")

a = int("34")  # a = 34
a = int("0100", 2)  # a = 4
a = int(6.7)  # a = 6
b = int("0xfe76214", 16)  # long b=266822164L
b = int("70", 8)  # b=56
b = float("3")  # b = 3.0
c = eval("3, 5, 6")  # c = (3,5,6)
c = eval("3 + 5 + 6")  # c = 14
print(f"Casting to specific type using general function: int('0100', 2) = 4\tint('0xfe76214', 16) = long b=266822164L",
      "\nint('70', 8) b=56\tfloat('3') b = 3.0\teval('3, 5, 6') c = (3,5,6)\teval('3 + 5 + 6') c = 14\n")

# This prints out "Hello, John!“
name = "John"
print("Hello, %s!" % name, ' Pring Hello John using %s string')

# This prints out "John is 23 years old. "
name = "John "
age = 23
print("%s is %d years old." % (name, age), ' Using %d digits')

# This prints out "John is 23 years old. Your sallary is 999.990 $"
name = "John"
age = 23
salary = 999.99
print("%s is %d years old. Your sallary is %.3f $" % (name, age, salary), ' Using %3f float')
print('%x/%X - Integers in hex representation (lowercase/uppercase)')

# default(implicit) order
default_order = "{}, {} and {}".format('John', 'Bill', 'Sean')
print('Default order using format function', "format('John', 'Bill', 'Sean')", default_order)
# order using positional argument
positional_order = "{1}, {0} and {2}".format('John', 'Bill', 'Sean')
print('Positional order using format function', "format('John', 'Bill', 'Sean')", positional_order)
# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John', b='Bill', s='Sean')
print('Using keyword argument format function', "format(j='John', b='Bill', s='Sean')", keyword_order)

# formatting integers
print("Binary representation of {0} is {0:b}".format(12))
'Binary representation of 12 is 1100'
# formatting floats
print("Exponent representation: {0:e}".format(1566.345))
'Exponent representation: 1.566345e+03'
# round off
print("One third is: {0:.3f}".format(1 / 3))
'One third is: 0.333'

str = 'programiz'
print('str = ', str)
# first character
print('str[0] = ', str[0])
# last character
print('str[-1] = ', str[-1])
# slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])
# slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])
