#Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string. Sample string:'w3resource'
#Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

str = 'hetvi'
my_dic={}
for letter in str:
    my_dic[letter]=my_dic.get(letter,0)+1
print(my_dic)
