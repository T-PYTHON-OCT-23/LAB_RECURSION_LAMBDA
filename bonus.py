def fizz_buzz_buzzel(num1 , num2) -> print:
    for n in range(num1,num2):
        if n%4 == 0 and n%3 == 0:
            print("FizzBuzz")
            continue
        
        if n%3 == 0:
            print("Fizz")
            continue
        elif n%4 == 0:
            print("Buzz")
            continue
        print(n)

# here we give it a number in between 1 and 100, you can do
fizz_buzz_buzzel(1,100)