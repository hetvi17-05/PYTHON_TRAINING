#l1 = [10,20,30,40,50]
"""
l1.append(200)#append will only add num from back
l1.insert(2,23)#to add num bettween list then use insert
"""
#l1.append(l2)#it will create list in list --> eg :[10, 20, 30, 40, 50, [20, 56, 80]]
#l1.extend(l2)#it will merge 2 list --> eg : [10, 20, 30, 40, 50, 20, 56, 80]
"""a = [1,2,3,4,100]
a.pop(2)
a.remove(100)
print(a)"""
"""
l = []
l1=[10,20,30,40,50]
for i in l1:
    if i not in l: # l ma kai na hoi toh aa use karvu 
        l.append(i)
print(l)
"""
"""for i in range(1,100):
    l.append(i)#sequence ne column ma leva 
print(l)"""

#l = ["hello"]

"""def append_list():
    l1 = ['hetvi']
    l2 = ['sheth']
    for i in l2:
        l1.append(i)
    print(l1)
append_list() 
----> output : ['hetvi','sheth']"""

"""
l = ['hetvi']
l1 = ['sheth']
for a,b in zip(l,l1):
    print(a,b) 
-----> hetvi sheth"""
"""
l1=['hetvi']
l2=['sheth']

print(l2)"""

