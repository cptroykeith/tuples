'''
x = ('Glean', 'sally', 'joseph')
print(x[2])

y = ( 1, 9, 2 )
print(y)
print(max(y))
for iter in y:
    print(iter)
    '''
  #sorting lists of tuples
d = {'a': 10, 'b':1, 'c':22}
t = sorted(d.items())
for k, v in sorted(d.items()):
    print(k, v)
#sorted by value instead of key
c = {'a': 10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
    tmp.append( (v, k) )
print(tmp)
tmp =sorted(tmp,reverse=True)
print(tmp)
#shorer version
c = {'a': 10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in c.items() ] ))
