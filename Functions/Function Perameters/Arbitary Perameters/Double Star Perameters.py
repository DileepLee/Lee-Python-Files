def add(**a) :
    print(a)
    print(type(a))
    print(len(a))
add()

# This Double star perameters are take the type as a Dictionary.
# If you pass the non Keyword arguments it will take it as a values, but Dictionary should store the data in the form of KeyValues.
# Thats while we geting the Error Message.

""" def add(**a) :
    print(a)
    print(type(a))
    print(len(a))
add(10,20,30) """

# So we want to store the arguments like keyvalues that is called as a keyword arguments.

def add(**a) :
    print(a)
    print(type(a))
    print(len(a))
add(a=10, b=20,c=30, d=40, e=50)

# So in this type keyvalues we can store many...
# ** Arbitary perameters compalsary we should pass the keyword Arguments.