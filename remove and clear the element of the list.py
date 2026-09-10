a=[2,34,5,67,39]
b=[34,34,4,3]
a.remove(34)# remove given value
x=b.pop(-1)#remove through indexing but return the value
print(x)
del(a[1:3])# remove through indexing but not return the value also delete the multiple element
print(x)
print(a)
print(b)
b.clear()#remove all the element of the given list 
print(b)
