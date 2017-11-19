def printinfo(str):
    print("this function will print in the console")
    print(str)
    return

printinfo(str='Hello World')

#variable function calling

def printagain( arg1 , *vartuple):
    print("this is a variable lenght arguement calling")
    print(arg1)
    for i in vartuple:
        print(i)
    return

printagain("this is a arguement")
printagain(20,30,40)

def func( list1 ):
    list1.append(100)
    return

list1 = [10,20,30]

func(list1)
print("Final list after the calling finish is ", list1)



def sum (a ,b):
    total = a + b
    return total

sum1 = sum(10,20)
print ("the sum of two numbers is ", sum1)
