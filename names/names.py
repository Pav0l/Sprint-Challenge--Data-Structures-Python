import time
from sort import merge_sort
from search import binary_search

start_time = time.time()

f = open('names\\names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names\\names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# Naive solution with runtime complexity of O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# Solution using dict/hash tables with runtime complexity of O(n)
"""
first_names = {}
# save every name from first file in a dict
for name_1 in names_1:
    first_names[name_1] = name_1

for name_2 in names_2:
    # for every name in list 2, check if it exist in the dict
    try:
        if first_names[name_2] == name_2:
            # if you find it, append it to duplicates arr
            duplicates.append(name_2)
    # if it doesnt exist, you get a KeyError and you continue
    except KeyError:
        pass

"""

# STRETCH USING ONLY ARRAYS AND SUB QUADRATIC TIME COMPLEXICITY

# Solution using merge sort [O(n * log n)] to sort the array and then binary search
names_1 = merge_sort(names_1)

# Do binary search in sorted names_1 list for every element in names_2 list
for name_2 in names_2:
    arr = names_1
    tar = name_2
    if binary_search(arr, tar):
        duplicates.append(name_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
