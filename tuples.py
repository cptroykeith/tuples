'''
x = ('Glean', 'sally', 'joseph')
print(x[2])

y = ( 1, 9, 2 )
print(y)
print(max(y))
for iter in y:
    print(iter)
    '''
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
'''

#exercises(five common words)
fname = input('Enter file: ')
if len(fname) < 1 : fname = 'intro.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1
#print(di)

tmp = list()
for k,v in di.items() :
    newt = (v,k) 
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)

for v,k in tmp[:5] :
    print(k,v)
    
