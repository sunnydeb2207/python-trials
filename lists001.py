mylist = [1, 2, 3, 4]
print(mylist)
print(mylist[1:3])
print(mylist[2:])

mylist[2] = 45
print(mylist)

mytuple = (1,2,3,4,5)
print(mytuple)
print(mytuple[2])
#mytuple[2] = 45    #Exception is given because tuple is immutable
#print(mytuple)

mylist01 = [mylist, 66, 77]
print(mylist01)
print(mylist01[[0][0]:2])
print(mylist01[0][0:3])

mytuple01 = (mytuple, mytuple, 3, 4, 5)
print(mytuple01)


#myset = set(12,11,222,33)

s = 123
print(list[s])