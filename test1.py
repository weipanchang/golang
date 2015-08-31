#!/usr/bin/env python

#print [(a,b,c) for a in range(1,1000) for b in range(a, 1000) for c in range(b,1000) if (a ** 2) + (b**2) == (c**2) and a+b+c==1000 ]
print len(set([a ** b for a in range(2, 6) for b in range(2,6)]))
#def Fibon(i):
#    if i == 1 or i == 2: return 1
#    return Fibon(i-1) + Fibon(i-2)
#l = [1,1]
#n = 3
#while 1:
#    l.append(l[n-2]+ l[n-3])
#    if len(str(l[n-1])) >=1000:
#        print n, l[n-1]
#        break
#    
#    n += 1


#n=2
#while 1:
#    l=[[] for i in range(6)]
#
#    for i in range(1,7):
#        for j in range(len(str(n*i))):
#                l[i-1].append(str(n*i)[j])
#        l[i-1].sort()
#   
#    if l[0] == l[1] == l[2] == l[3] == l[4] == l[5]:
#        print n, l
#        break
#    n += 1
#

#l = [(a,b,c) for a in range(-45,46) for b in range(-45,46) for c in range(-45, 46) if (a **2 + b**2 + c**2) == 45 * 45]
#print l
#sum1 = 0
#for i in range(len(l)):
#    sum1 += abs(l[i][0]) + abs(l[i][1] ) + abs(l[i][2])
#print(sum1)
    