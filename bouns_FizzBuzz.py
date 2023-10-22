def fizzbuzz_while(num1 , num2):
    while num1 != num2 :
        num1 +=1
        if num1 % 5 == 0 and num1 % 3 == 0:
            print("FizzBuzz")
        elif num1 % 3 == 0:
            print("Fizz")
        elif num1 % 5 == 0:
            print("Buzz")
        else:
            print(num1)        
print("----Exercise: FizzBuzz by use while ------")
fizzbuzz_while(1,100)

def fizzbuzz_for (num1,num2):
    range(num1 , num2+1)
    for num in range(num1 , num2+1):
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
print("----Exercise: FizzBuzz by use for ------")       
fizzbuzz_for(1,100) 