def find_duplicates(elements):
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)
print(find_duplicates())
# Not complete but try and complete it
'''
Remove all
duplicates from
list
'''