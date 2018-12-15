import random
import math


def r(v):
        return random.randint(1, v)


def good():
        return [r(12),r(12),r(2)]

def bad():
        return [r(6)]

def diceTest():
        d = dict()
        for i in range(60000):
                v = r(6)
                if v not in d:
                        d[v] = 0
                d[v] = d[v]+1

        print(d)


def testAnyTheory(theory,n=100000):
        s = 0
        p = 0
        z = 0

        for i in range(n):
                t = theory()
                if t is 0:
                        z+=1
                elif t>0:
                        p+=1
                s = s + t
                
        #print(s/n,p,z,n-p-z)
        
        return [s/n,p,z,n-p-z]


def theory1():
        g = good()
        b = bad()
  
        c = g + b
   
        t = sum(c)-max(c)
        #print(g,b,sum(g),t, t - sum(g))

        return t - sum(g)




def theory2():
        g = good()
        b = bad()

        #print(g,b, max(g), max(b), "#", min(max(g), max(b)),sum(g))

        t = sum(g+b) - min(max(g), max(b))       

        return t - sum(g)




def theory2b():
        g = good()
        b1 = bad()
        b2 = bad()

        #print(g,b, max(g), max(b), "#", min(max(g), max(b)),sum(g))
        
        m = [max(g),max(b1),max(b2)]
        t = sum(g+b1+b2) - sum(m) + max(m)
        #print(g,b1,b2,"#",m)

        #t = sum(g+b) - min(max(g), max(b))       

        return t - sum(g)

def tc(s,g):
        if s<9:
                return -1*g
        if s<13:
                return math.floor(g/2.0)
        else:
                return g

def theory0():

        b = [r(12),r(12),r(12)]

        s = sum(b)

        f = tc(s,1)

        #print(b,s,f)

        return f

def makeTheory0(d,g):
        print(d,g)
        def theory():
                # id_list = [x.id for x in original_list]
                b = [r(x) for x in d]
                
                s = sum(b)

                f = tc(s,g)
                #print(d,b,s,f)
                return f
        return theory



diceTest()



print(testAnyTheory(theory2))

print(testAnyTheory(theory2b))

print(testAnyTheory(theory0))

print()

for g in range(1,7):
        tat = testAnyTheory(makeTheory0([12,12,12],g))
        print(tat)
        print(tat[0]/g)
        print()

for d in range(2,14,2):
        g = 2
        tat = testAnyTheory(makeTheory0([12,d],g))
        print(tat)
        print(tat[0]/g)
        print()

for d in range(2,14,2):
        g = 1
        tat = testAnyTheory(makeTheory0([12,d],g))
        print(tat)
        print(tat[0]/g)
        print()
