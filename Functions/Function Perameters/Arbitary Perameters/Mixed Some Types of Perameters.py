def add(a, *b) :
    print(a)
    print(b)
add(10,20,30,40)

# Whenever we run this code the 10 value is given to 'a' peramete and 20,30,40 is given to 'b' perameter.

"""
# Example 2
def addd(*a,b) :
    print(a)
    print(b)
addd(10,20,30,40) """
# Here We got the Error...Because all the arguments values are given to a perameters, but not be given any values in b.

# Example 3
def ad(*a, b=123) :
    print(a)
    print(b) 
ad(10,20,30,40) # Here if you need the b value also you can give here....like this.
ad(10,20, b=50)