x = "python is a opensource language"
print(x)
words = x.split()
p = [[w.upper(), w.lower(), len(w)] for w in words]
for q in p:
    print(q) 

                   #or
#This is Comprehensive method like to write one line or less line code in python by using pyhton

for q in [[w.upper(),w.lower(),len(w)] for w in "python is a opensource language".split()]:print(q)