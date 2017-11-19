try:
    file = open("foo2.txt","r")
    file.write("this is an exception hadling example")
except IOError:
    print("the file can't be open for the writing")
else:
    print("content written succesfully")
finally:
    print("end of the operation")


# Define a function here.
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
          print("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz");

