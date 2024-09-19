import copy

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

print("--- Start ---")
print("The all() function returns True if all items in an iterable are true, otherwise it returns False.")
list1 = [True, True, True]
ml1 = all(list1)
print(f"list1: {list1}")
print(f"My list all(): {ml1}")

list2 = [10, 1, 33, 24, 56, 78, 99, 24]
ml2 = all(list2)
print(f"list2: {list2}")
print(f"My digital list all(): {ml2}")

dict1 = {0: "Apple", 1: 0, 3: "Run", True: True}
md1 = all(dict1)
print(f"dict1: {dict1}")
print(f"My dict all(): {md1}")
print("---")

list3 = ["One", "Second element", 3, 'Four', ['inner_arr_val_1', 'inner_arr_val_2', 'inner_arr_val_3']]
print(f"list3: {list3}")
print(f"list3[0] : {list3[0]}")
print(f"list3[2] : {list3[2]}")
print(f"list3[4][1] : {list3[4][1]}")
print(f"list3[-1] : {list3[-1]}")
print(f"list3[1:3] : {list3[1:3]}")
print(f"list3 + list1 : {list3 + list1}")
print(f"list2 * 3 : {list2 * 3}")
print(f"\nlist2: {list2}")
print(f"33 in list2 : {33 in list2}")
print(f"34 in list2 : {34 in list2}")
print(f"list2==list1 : {list2 == list1}")
print(f"list2[1:6:2] : {list2[1:6:2]}")
print(f"list2[::-2] : {list2[::-2]}")
print(f"list2[::-1] : {list2[::-1]}")
print(f"list2.count(24) : {list2.count(24)}")
print(f"list2.append(88) : {list2.append(88)} list2: {list2}")
print(f"list2.sort() : {list2.sort()} list2: {list2}")
print(f"list2.index(88) : {list2.index(88)}")
print(f"list2.append([3,5]) : {list2.append([3, 5])} list2: {list2}")
print(f"list2.extend([3,5]) : {list2.extend([3, 5])} list2: {list2}")
print(f"list2.pop() : {list2.pop()} list2: {list2} ___ Remove and return element ___")
print(f"list2.remove(99) : {list2.remove(99)} list2: {list2} ___ Remove and do not return nothing ___")
print("---")

l1 = [4, 33, 25]
l2 = l1
l3 = l1[:]
print(f"list l1: {l1}, ID: {id(l1)}")
print(f"list l2: {l2}, ID: {id(l2)}")
print(f"list l3: {l3}, ID: {id(l3)}")
l1[2] = 'some'
print("Set l1[2] = 'some'")
print(f"list l1: {l1}, ID: {id(l1)}")
print(f"list l2: {l2}, ID: {id(l2)}")
print(f"list l3: {l3}, ID: {id(l3)}\n")

lb1 = [4, 33, [2, 5, 3]]
lb2 = lb1
lb3 = lb1[:]
print(f"list l1: {lb1}, ID: {id(lb1)}")
print(f"list l2: {lb2}, ID: {id(lb2)}")
print(f"list l3: {lb3}, ID: {id(lb3)}")
lb1[2][1] = 'some'
print("Set lb1[2][1] = 'some'")
print(f"list lb1: {lb1}, ID: {id(lb1)}")
print(f"list lb2: {lb2}, ID: {id(lb2)}")
print(f"list lb3: {lb3}, ID: {id(lb3)}")
print("\tSurface copy ([:]) copies only the list itself, but does not copy nested objects. \n\
Therefore, if a list has nested structures, like other lists, then changes to the nested structures will be reflected in all copies.\n---")

# Original list with nested elements
original_list = [4, 33, [2, 5, 3]]

# Perform a deep copy
copied_list = copy.deepcopy(original_list)

# Modify the original list
original_list[2][1] = 'some'

# Output the lists and their IDs
print(f"Original list: {original_list}, ID: {id(original_list)}")
print(f"Copied list: {copied_list}, ID: {id(copied_list)}")

# Check inner lists
print(f"Original inner list: {original_list[2]}, ID: {id(original_list[2])}")
print(f"Copied inner list: {copied_list[2]}, ID: {id(copied_list[2])}")

print(f"len(copied_list): {len(copied_list)}")
del original_list[2]
print(f"max(original_list): {max(original_list)}, original_list: {original_list}")
print(f"Add to original_list 8 {original_list.append(8)}, original_list: {original_list}")
original_list.pop()
print(f"original_list.pop(), original_list: {original_list}")
print("---")

print("The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.")
x = ['apple', 'banana', 'cherry']
print(f"x: {x}")
y = enumerate(x)
print("enumerate(x): ", list(y))
print("---")

newColl = ['Hello', 'World']
print(f"x: {x}, \tnewColl: {newColl}")
newColl.extend(x)
print(f"newColl.extend(x) \tneColl: {newColl}")

print("")
newColl2 = [item for item in newColl]
print(f"newColl2 = [ item for item in newColl ] \tnewColl2: {newColl2}")
print(f"")

list1 = [1, 2, 3, 4, 5]
list2 = [item for item in list1 if item > 2]  # Додаємо тільки елементи, які більше 2
print(f"list1: {list1}")
print(f"list2 = [item for item in list1 if item > 2], list2: {list2}")

result = [2 not in list1]
print(f"2 not in list1 result: {result}")

for fruit in ['apple', 'banana', 'mango']: print("I like", fruit)
print("---\n")

print("Tuples")
t = (1, 24, 55, 83, 97)
print(f"t: {t}, type(t): {type(t)}")
print(f"convert tuples to list: tl = list(t)")
tl = list(t)
print(f"tl: {tl}, type(tl): {type(tl)}")
tl.append(('one', 'two', 'three'))
print(f"tl.append(('one', 'two', 'three')), tl: {tl}")
for i in tl:
    print(f"Type value in tuple: {type(i)}")
print("---")
print(f"tl.count(55): {tl.count(55)}")
print(f"tl.index(55): {tl.index(55)}")
