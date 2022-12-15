#*args:(arguments or tuple as a parameter) and **kwargs:(key with arguments or dictionary as a paramter)
#syntax : args
#def funname(*args):
    #statment
#(tuple as a parameter)
def myfun(*args):
    sum = 0
    for i in args:
        sum+=i
    print(sum)

myfun(12,23.34,45,56)    

