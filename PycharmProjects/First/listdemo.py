#list functionality
list = ['physics','maths','cheistry']

print(list[0])
print(list[1])
print(list[2])

#delet function
del list[2]
print(list)

#lenght of the list
print(len(list))

#concatenation of the list
list1 = ['100','200','300']
print(list + [123])
print(list + list1)

#generatinng the list
print(list * 2)

#comparing the value of the string
list3 = ['abc','abd','abf']
print(max(list3))
print(list3)

#append to the lisy
list3.append(2050)
list3.append('abc')

print(list3)

print(list3.count(2050))


list4 = [123,123]
list5 = [432,435]
list4.extend(list5)
print(list4)

aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print("Extended List : ", aList)

list5 = [12,13,14]
list6 = [23,34]
list5.insert(1,123)
print(list5)

list7 = [12,13,13,12,14,15,16]
print(list7.count(12))

list8 = []
print(list8.count(0))

print("the index of the 12 is ",list7.index(12,1,5))

print("the pop od the list 8 is", list7.pop(4))

print("the list is",list7)

print("removed the element from the list", list7.remove(14))

print(list7)
