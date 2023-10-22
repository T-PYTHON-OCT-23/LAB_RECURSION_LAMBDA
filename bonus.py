def fizzBuzzFor():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
#fizzBuzzFor() 

def fizzBuzzWhile():
    increment=1
    while increment!=101:
        if increment%3==0 and increment%5==0:
            print("FizzBuzz")
        elif increment%3==0:
            print("Fizz")
        elif increment%5==0:
            print("Buzz")
        else:
            print(increment)
        increment+=1
#fizzBuzzWhile()



