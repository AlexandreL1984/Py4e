#Py4E Chapter 10 Tuples
#Even ShorterVersion
#List Comprehension creates a dynamic list

c = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in c.items() ] ) )
