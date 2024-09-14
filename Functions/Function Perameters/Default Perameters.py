def add(a=100, b=200):
    c = a+b
    print(c)
add()
# if we gives here some value in function name it will take that type of key values like...
add(1000)
add(10,20)

# Default perameters means you need not to pass the values of the time of calling function..

def badass(a, b=1000):
    c = a+b
    print(c)
badass(500)
badass(100,200) 

# ..........OR..........

# whenever we use this type of code like default perameter it will not execute. its Displays Error Message.
"""def addd(a=100, b) :
    c = a+b
    print(c)
addd(1000)
addd(100,200) """
