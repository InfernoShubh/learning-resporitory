list=[2,4,6,8]
empty_list=[]
empty_list.append(list)
product=1
add=0
for i in list:
       product*=i
       add+=i
print(add/len(list))       
print(product)
print(empty_list)
