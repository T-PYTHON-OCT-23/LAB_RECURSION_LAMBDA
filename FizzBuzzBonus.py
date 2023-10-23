number = range(1,100)
counter = 0

print("for loop")
print()

for num in number:
    if num % 3 == 0:
        print("Fizz")
    if num % 5 == 0:
        print("Buzz")
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    else:
        print(num)


print("While loop")
print()


while number != 0 :
            counter +=1
            if number % 3 == 0:
                print("Fizz")

            if number % 5 == 0:
                 print("Buzz")

            if number %3==0 and number %5==0:
                 print("FizzBuzz")
            else:
                print(number)

