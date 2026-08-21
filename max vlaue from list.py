a=["67","2","34","79","45"]
print(max(a))
max=a[0]
for i in a:
    if i>max:
        max=i
print(max,"largest value")
