import matplotlib.pyplot as plt

x1 = 0.4846916
y1 = -2.103407
x2 = -0.03745484
y2 = -2.248116

koefx = y1-y2
koefy = x2-x1
koef = x1*y2 - x2*y1

print ( f'({koefx})x + ({koefy})y + ({koef}) = 0;' )

def subx(x):
    return (((-1*koef)-(koefx * x))/ (koefy)) #mengembalikan nilai y

def suby(y):
    return (((-1*koef)-(koefy * y))/ (koefx)) #mengembalikan nilai x

x=x1
y=y1

def proc(a,b):
    c=0
    if a == b:
        c=0
    elif a < b:
        c = 0.001
    else :
        c = - 0.001
    return c

def check(a,b):
    if(a > b + 0.001):
        return True
    elif(a < b - 0.001):
        return True
    else:
        return False

xarr = []
yarr = []

while (True):
    if (x1 == x2):
        res = proc(y1,y2)
        y += res
        xarr.append(x)
        yarr.append(y)
        print(f"({x},{(y)})")
        if(not check(y,y2)):
            break
    elif(y1==y2):
        res = proc(x1,x2)
        x += res
        xarr.append(x)
        yarr.append(y)
        print(f"({x},{(y)})")
        if(not check(x,x2)):
            break
    else:   
        res = proc(x1,x2)
        x += res
        
        xarr.append(x)
        yarr.append(subx(x))
        
        print(f"({x},{subx(x)})")
        if(not check(x,x2)):
            break

 
plt.scatter(xarr, yarr)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('My first graph!')
  
# function to show the plot
plt.show()

# print(xarr)
# print(yarr)
