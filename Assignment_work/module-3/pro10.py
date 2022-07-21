#Write a Python program to find the second smallest number in a list.
list_of_numbers = [2, 1, 9, 8, 6, 3, 1, 0, 4, 5]
  
def SecondSmallest(lst):
    firstSmallest = min(lst[0],lst[1])
    secondSmallest = max(lst[0],lst[1])
    for i in range(2,len(lst)):
        if lst[i] < firstSmallest:
            secondSmallest = firstSmallest 
            firstSmallest = lst[i]
        elif lst[i] < secondSmallest and firstSmallest < lst[i]:
            secondSmallest = lst[i]
    return secondSmallest 

print(SecondSmallest(list_of_numbers))