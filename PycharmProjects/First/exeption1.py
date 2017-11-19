def levelchek(level):
    if level < 1:
        raise Exception(level)
    else:
        print("the level is" , level)
        return level

try:
    i = levelchek(-1)
    print("the level passed is ",i)
except Exception as a:
    print ("the exception araises is ", a)