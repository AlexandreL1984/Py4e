#py4e Chapter 14
#Object Oriented Programming, OOP

stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print (stuff[1])

print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))

#this is me practicing the dir function
dir(stuff)

#this is me getting familiar with some methods listed in the dir function
stuff.append('Json')
stuff.append('Alex')
stuff.copy()
stuff.index('Alex')
stuff.reverse()
print (stuff)
stuff.index('Json')
stuff.pop()
print (stuff)
stuff.pop()
print (stuff)
