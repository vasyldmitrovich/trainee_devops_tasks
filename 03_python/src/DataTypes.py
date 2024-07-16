print("Start learning data types")

bool_var = True
int_var = 12
float_var = 12.5
list_var = ['abcd', 786, 2.23, 'john', 70.2]
tuple_var = ('abcd', 786, 2.23, 'john', 70.2)
str_var = "My name is ..."
# set_var = set('qwerty') => set(['e', 'q', 'r', 't', 'w', 'y'])
frozenset_var = frozenset('qwerty')
dict_var = {'name': 'john', 'id': 6734, 'role': 'admin'}

print("bool_var: ", bool_var, " \tint_var: ", int_var, " \tfloat_var: ", float_var,
      " \nlist_var: ", list_var, " \ntuble_var: ", tuple_var, " \tstr_var: ", str_var, " \nfrozenset_var: ",
      frozenset_var,
      " \ndict_var: ", dict_var, "\n")

print("Id immutable variable 'int_var' before changing: ", id(int_var))
int_var = 132
print("Id immutable variable 'int_var' after changing: ", id(int_var), "\n")

print("Id mutable variable 'list_var' before changing: ", id(list_var), f"\n {list_var}")
list_var.append('bla')
print("Id mutable variable 'list_var' after changing: ", id(list_var), f"\n {list_var}", "\n--- End ---\n")

a = 10
b = a
print("If a=10 and b = a")
print(f"a: {a}: id: ", id(a), f"b: {b}: id: ", id(b))
b += 1
print(f"a: {a}: id: ", id(a), f"b: {b}: id: ", id(b))
a += 1
print(f"a: {a}: id: ", id(a), f"b: {b}: id: ", id(b), "\n")  # Because a number between -5 and 256 is cached by Python
# to optimize memory, so all variables assigned these values refer to the same object in memory.

d = 1000
k = d + 1
print("If d=1000 and k = d+1")
print(f"d: {d}: id: ", id(d), f"k: {k}: id: ", id(k))
d += 1
print("If d+=1 ")
print(f"d: {d}: id: ", id(d), f"k: {k}: id: ", id(k))  # Numbers bigger than 256 do not cached
# each time a new value is assigned, a new object is created in memory with a new ID.

x = 1.0
y = x
print(f"x: {x}, id: {id(x)}, y: {y}, id: {id(y)}")

y += 1.0
print(f"x: {x}, id: {id(x)}, y: {y}, id: {id(y)}")
# Fractional numbers are not cached like some integers,
# so every time a new float value is created, a new object is created in memory.

list1 = [1, 2, 3]
list2 = list1
print(f"list1: {list1}, id: {id(list1)}, list2: {list2}, id: {id(list2)}")

list2.append(4)
print(f"list1: {list1}, id: {id(list1)}, list2: {list2}, id: {id(list2)}")
# Lists are mutable, and when you assign a list to another variable, both variables refer to the same object in memory.

tuple1 = (1, 2, 3)
tuple2 = tuple1
print(f"tuple1: {tuple1}, id: {id(tuple1)}, tuple2: {tuple2}, id: {id(tuple2)}")

tuple2 = tuple2 + (4,)
print(f"tuple1: {tuple1}, id: {id(tuple1)}, tuple2: {tuple2}, id: {id(tuple2)}")
# Tuples are immutable, so a new tuple is created every time its contents change.

str1 = "hello"
str2 = str1
print(f"str1: {str1}, id: {id(str1)}, str2: {str2}, id: {id(str2)}")

str2 += " world"
print(f"str1: {str1}, id: {id(str1)}, str2: {str2}, id: {id(str2)}")
# Strings are immutable. Short strings can be cached, as can small integers.

set1 = {1, 2, 3}
set2 = set1
print(f"set1: {set1}, id: {id(set1)}, set2: {set2}, id: {id(set2)}")

set2.add(4)
print(f"set1: {set1}, id: {id(set1)}, set2: {set2}, id: {id(set2)}")
# Sets are mutable, so a new set is created each time its contents change.

dict1 = {'a': 1, 'b': 2}
dict2 = dict1
print(f"dict1: {dict1}, id: {id(dict1)}, dict2: {dict2}, id: {id(dict2)}")

dict2['c'] = 3
print(f"dict1: {dict1}, id: {id(dict1)}, dict2: {dict2}, id: {id(dict2)}", "\n---")
# Dictionaries are mutable, so a new dictionary is created every time its contents change.

'''
Small integers and short strings can be cached, so variables assigned to these values can have the same identifiers.
Fractional numbers, tuples, lists, sets, and dictionaries are not cached in this way, 
and each time a new value or object is created, a new ID is created.
Variable data types (lists, sets, dictionaries) retain their identifier when their contents change, 
if they are changed through object methods. But if a new object is assigned to a variable, the identifier changes.
'''

type_is = type(dict2) is dict
print("Variable 'dict2' is or not type disc: ", type_is, "\n---")

z = 1 + 2 + 3 + \
      4
print(f"z is: {z}")
z = (1 + 2 + 3 + 4 + 5)
type_z = type(z)
print(f"z = (1 + 2 + 3 + 4 + 5) is: {z}", type_z)
z = [ 1 + 2 + 3 + 4 + 5 + 6]
type_z = type(z)
print(f"z = [ 1 + 2 + 3 + 4 + 5 + 6] is: {z}", type_z)
z = { 1 + 2 + 3 + 4 + 5 + 4 + 3, 23, 22}
type_z = type(z)
print("z = { 1 + 2 + 3 + 4 + 5 + 4 + 3, 23, 22} is: ", z, type_z, "\n")