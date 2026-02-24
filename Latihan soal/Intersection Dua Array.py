def intersection(list1, list2):
    set2 = set(list2)
    return [item for item in list1 if item in set2]

# Contoh
print(intersection([1,2,3,4], [3,4,5,6]))
