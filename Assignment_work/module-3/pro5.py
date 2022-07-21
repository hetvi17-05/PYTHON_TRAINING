#write a python function that takes two list and return true if they have at least one common member.
def  common_member(list1,list2):
    status = False
    for x in list1:
        for y in list2:
            if x==y:
                status = True
                return status
print(common_member([1,2,3,4,5,6], [5,6,7,8]))
print(common_member([1,2,3,4,5], [6,7,8,9]))
            
