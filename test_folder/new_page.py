'''
if 5 > 2:
    print('welcome to 2024, My year of double exploit')
    x="math"
    
    #is the same thing as 
    x='math'
    i,j,k='ink','mathematics','mate' #this is allowed in python for declaring three different variable at once
    t=y=u="welcome to 2024" #this means that t,y,u contains welcome to 2024
    #outputing varibles
    
x="awesome" 
print('python is ' + x)
    

 #adding varuables
a="python is very "
s="awesome"
w=a+s
print (w)
     #if one of the var contains int and the other contains string then python will return error

     #global variables 

x="mathematicians"
def myfunc():
    print('python is for' + x)

myfunc()


w='the class of 300'
def mydef():
    w="math"
    print('python needs ' + w) 

mydef()

        #the output is python needs maths, because functions use the values in local var if a global var has the same name
        
        #to creat a global variable inside a funtion you will have to use the global keyword
def myfunc():
    global x
    x="mathematician"
myfunc()
print('python can also be use by ' + x)

x,y,z = "orange","apple",'mango'
print(x)
print(y)
print(z)
x= 1j
print(type(x))

y=['mary','ken','matt','uche']  #this is a list
x=('mary','matt','uche','ken') #this is a tuple names
z={'mary','matt','uche','ken'} #this is a set
k ={"name":"mary","surname":"matt","age":25} #this is a disc 
m = frozenset({"mary","ken","uche",'benny'})

print(x)
print(y)
print(z)
print(k)
print(m)

#to convert from one data type to another
x =1
y= 2.5
z=1j

a=float(x)
b=int(y)
c=complex(x)

print(type(a))
print(type(b))
print(type(c))
print(a)
print(b)
print(c)'''

#how to print random numbers in python
import random
print(random.randint(1,100))
#OR
print(random.randrange(1,100))

