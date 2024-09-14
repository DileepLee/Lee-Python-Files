def greet(name,msg) :
    print("Hello",name,msg)
greet(name="Dileep",msg="Good Morning")
greet(msg="Dileep", name="Good Morning")
greet("Godd Morning", msg="Dileep")

# Here these function names and Arguments are not Executed,... 
#because Positional arguments follows keyword Arguments.
# And greet() function got multiple values for argument 'name'.

"""greet(name="Dileep", "Good Morning")
greet("Good Morning", name="Dileep")"""