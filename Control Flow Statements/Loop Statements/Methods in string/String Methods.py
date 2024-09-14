# This Method is to split the words for the string objects...and to divided thje etair string in the form of multiple words based on the specified delimiter.

x = "Python@is@a@open@source@language"
print(x)
words = x.split("@")
for w in words :
    print(w.upper(),w.lower(),len(w))