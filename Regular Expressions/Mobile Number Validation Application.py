import re
regex = re.compile (r" \d(10)")
while True :
    mobno = input("Enter Mobile Number : ")
    if len(mobno) == 10 :
        result = regex.search(mobno)
        if result :
            print("Valid Mobile Number")
            break
        else :
            print("Mobile number should contain digits only")
    else :
        print("Invalid Mobile Number")