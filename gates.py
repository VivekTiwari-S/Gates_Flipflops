# Basic Gates

def And(a,b):
    return a & b
def Not(a):
    return not a
def Or(a,b):
    return a | b
    
a = int(input('Enter a : '))
b = int(input('Enter b : '))

print(And(a,b))
print(Not(a))
print(Or(a,b))

# SR Flipflop

def sr(s,r,q):
    return (q and not r) or s

s,r,q = map(int,input('Enter s,r,q : ').split())
if s == 1 and r == 1:
    print('Invalid !')
else:
    print('Qnext : ', sr(s,r,q))
