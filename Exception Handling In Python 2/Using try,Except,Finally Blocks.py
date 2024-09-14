x = None
try:
    x = open("Dileep.txt")
    print("file is Opened")
    print(x.read())
    x.write("DileepLee")
except:
    print("Error Occured")
finally:
    x.close()
    print("File is Closed")