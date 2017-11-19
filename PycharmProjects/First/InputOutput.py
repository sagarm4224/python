str = input("Enter the input \n")

print("received input is", str)

#file creation mode in PYTHON

file = open("foo1.csv","w+")
file.write("Python is so good nowadays, isn't it\n")


file = open("foo1.csv","r+")
str = file.read()
print("the read string is ", str)

position = file.tell()
print("the current position of the file is " , position )
file.close()


import os;
os.rename("foo1.csv","foo2.csv")

os.remove("foo2.csv")

os.rmdir("New DIrectory")
os.mkdir("New Directory")
print(os.getcwd())

file = open("foo.txt","r")

for index in range(5):
    line = file.__next__()
    print(index,line)

file.close()

file = open("foo.txt","r")

line = file.read(10)
print("the number of byte read is ", line)
file.close()

file = open("foo.txt","r")

for i in range(6):
    line1 = file.readline()
    print("the number of byte read is" , line1)

file.close()

file = open("foo.txt","r")
line = file.read()
print("the line read is ",line)

file.seek(7,0)
line = file.read()
print("after the seek the line read is ",line)



