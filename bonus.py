
#use for 
def FizzBuzz():
    for number in range(1,100):
        if number % 5 == 0 and number % 3 == 0 :
            print(f"{number} is FizzBuzz")
        elif number % 3 == 0:
            print(f"{number} is Fizz")
        elif number % 5 == 0:
            print(f"{number} is Buzz")

FizzBuzz()


 # use while       
def FizzBuzz_tow():
    numbers=1
    while numbers in range(1,100):
        if numbers % 5 == 0 and numbers % 3 == 0 :
            print(f"{numbers} is FizzBuzz")
        elif numbers % 3 == 0:
            print(f"{numbers} is Fizz")
        elif numbers % 5 == 0:
            print(f"{numbers} is Buzz")
        numbers+=1

FizzBuzz_tow()