'''
#local variable
def square(n):
    m = n*n
    return m
print("The square of 3 is ")
print(square(3))
print(m)


#global variable
a = 5
def func(b):
    c = a + b
    return c
print(func(4))
print(a)

#global variable
a = 5
def func(b):
    global a
    a=10
    c = a + b
    return c
print(func(4))
print(a)

#global variable
a = 5
def func(b):
    a=10
    c = a + b
    return c
print(func(4))
print(a)
#immutable and mutable datatypes      
def f1(x,y):
    x = x * 2
    y = y * 2
    print(x,y)

def f2(x,y):
    x = x * 2
    y[0] = y[0] * 2
    print(x,y)
a = 1
b = [2,3]
f1(a,b)
print(a,b)
f2(a,b)
print(a,b)



#function of functions
def calculate(x,f):
    return f(x)
def square(n):
    return(n*n)
def cube(n):
    return(n*n*n)
print(calculate(5,square))
print(calculate(5,cube))

#default arguments
def print_error(lineno, message='error'):
    print (f'{message} at line {lineno}')
print_error(10)
print_error(1,"no error")
print_error(message="no error",lineno=5)

#non-keyword multiple arguments
def myFun(*a):
    for x in a:
        print(f'Welcome {x}')
myFun('Ram','Tom','Sam')
myFun('sony')

#keyword multiple arguments
def myFun(**a):
    for x,y in a.items():
        print(f'{x}= {y}')
myFun(pin= 12034,name='Ram',class1="cse/csm/csc/ece/eee")
'''
#builtin functions
print(abs(-5))
print(max(2,-3,0,-5,4,-8))
print(chr(70))
print(ord('H'))
print(bin(10)[2:])
print(type(hex(10)))
print(oct(10))
print(sum([10,20]))
print(len((2,3,4,5)))
print(sorted('hello'))
print(",".join(list(reversed('hello'))))
l=[10,20,30,40,50]
fofor x,y in enumerate(l):
    print(x,y)

