def FizzBuzz_forloop(value1:int,value2:int)->int:
    for i in range(value1 , value2):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz",i)
        elif i % 3 == 0:
            print("Fizz",i)
        elif i % 5 == 0:
            print("Buzz",i)

def FizzBuzz_Whileloop(value1:int,value2:int)->int:
    count = value1
    while count <= value2:
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz",count)
        elif count % 3 == 0:
            print("Fizz",count)
        elif count % 5 == 0:
            print("Buzz",count)  
        else:
            print(count)
        count+=1

print("Program that displays numbers that are multiples of 3 and 5.")
val1 = int(input("Enter the first number in range: "))
val2 = int(input("Enter the last number in range: "))
#Fizz Buzz using for loop
print("---Fizz Buzz using for loop---")
FizzBuzz_forloop(val1,val2)
print("--"*20)
#Fizz Buzz using while loop
print("---Fizz Buzz using while loop---")
FizzBuzz_Whileloop(val1,val2)


