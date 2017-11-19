def function( level ):
    if level < 1:
        raise Exception (level)
    return level

try:
    l = function(-10)
    print ("the number level is ",l)
except Exception as e:
    print("error in level arguement",e.args[0])


