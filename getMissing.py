def getMissing(lst):
    return  set(range(lst[len(lst)-1])[1:]) - set(x)

x = list(range(1,100))
x.remove(50)
print(getMissing(x))
'''
Get missing
number in
[1...100]
'''