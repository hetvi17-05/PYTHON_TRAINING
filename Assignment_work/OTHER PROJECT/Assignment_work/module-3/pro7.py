#Write a Python function that takes a list and returns a new list with unique 
#elements of the first list
def unique_list(num):
    unique = []
    for item in num:
        if item not in unique:
            unique.append(item)
    return unique
print(unique_list([1,2,5,9,7,1,7,6]))
