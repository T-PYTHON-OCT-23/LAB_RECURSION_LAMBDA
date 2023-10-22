def fizFor():
    for i in range(1,101):
        temp=""
        if i%3==0:
            temp+="fizz"
        if i%5==0:
            temp+="Buzz"
        if temp!="":
            print(temp)

def fizWhile():
    i=1
    while i!=101:
        temp=""
        if i%3==0:
            temp+="fizz"
        if i%5==0:
            temp+="Buzz"
        i+=1
        if temp!="":
            print(temp)
        
        
