

print("----------<For loop>-----------")
for num in range(1,100+1):
    if num%3==0:
        print("Fizz",)
    if num% 5 ==0:
        print("Buzz",)
    if num%3==0 and num%5==0:
        print("FizzBuzz")



print("----------<while loop>-----------")
i=1

while i<=100:
    if i%3==0:
        print("Fizz",)
    if i% 5 ==0:
        print("Buzz",)
    if i%3==0 and i%5==0:
        print("FizzBuzz")

    i+=1



