def intersect(lst1,lst2):
    res, lst2_copy = [], lst2[:]
    for el in lst1:
        if el in lst2_copy:
            res.append(el)
            lst2_copy.remove(el)
    return res
'''
Compute
the
intersection
of two lists
'''