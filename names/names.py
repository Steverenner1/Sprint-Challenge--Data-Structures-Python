import time
from names_bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# The runtime complexity of the nested for loops was O(n2), causing it to run in approx 6 seconds.
# With refactoring using binary search tree, we are able to have the 2 for loops as linear O(n) instead of quadratic, causing a much shorter runtime of less than 1/100 of a second.

SearchTree = BinarySearchTree('names')

for names_one in names_1:
    SearchTree.insert(names_one)
for names_two in names_2:
    if SearchTree.contains(names_two):
        duplicates.append(names_two)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
