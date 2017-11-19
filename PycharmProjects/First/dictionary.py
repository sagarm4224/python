dic = {1:"sagar",2:"megha",3:"test"}

print(dic[1])

#update the existing query

dic[3] = "test1"

print(dic)

#add to the dictionary
dic[4] = "test2"

print(dic)

dic.clear()

print(dic)

#don't run the below comment unless its require
#del dic

#print(dic)

#tuples implementation

dic1 = {('top',1):'sagar'}

print(dic1)

print("the lenght of the dictionary is ", len(dic))

print("the string representation of the dictionary is %s" %str(dic1))

dic2 = dic1.copy()

print("the copy of the dictinary dic1 is", dic2)

#from keys values
seq = ('test','test2','test3')

seq1 = (10,20,30)

dict = dict.fromkeys(seq,seq1)



print(dict)

print(dict.get('test2'))

dict2 = {1: 'a', 2:'b',3:'c'}
print(dict2)

print("the items of the list are ", dict2.items())

print("the keys in the list are ", dict2.keys())

print("the values in the list are", dict2.values())

dict3 = {1:"value",2:"value2",3:"value3"}

print(dict3)

print("the default value of 4 is", dict3.setdefault(4,"None"))


dict4 = {5:'testwithnonsense'}

dict3.update(dict4)

print("the updated dictionary is", dict3)