
def fuzzBuzzInFor():
    for num in range(1, 100 +1):
        if num % 3 == 0 and num % 5 == 0:
         print(f"{num} --->FizzBuzz")
        elif num % 3 == 0:
         print(f"{num} -->Fizz")
        elif num % 5 == 0:
         print(f"{num} --->Buzz")


def fuzzBuzzInWhile():
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
         print(f"{num} --->FizzBuzz")
        elif num % 3 == 0:
         print(f"{num} -->Fizz")
        elif num % 5 == 0:
         print(f"{num} --->Buzz")
        num += 1


fuzzBuzzInFor()
fuzzBuzzInWhile()
         
         
    