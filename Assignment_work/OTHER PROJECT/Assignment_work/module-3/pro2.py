def compare (words):
    chr = 0
    for word in words:
        if len(word)>2 and word[0]==word[-1]:
            chr+= 1
print(compare(['abc','xyz','1234','iop','asdfghjghjk']))
