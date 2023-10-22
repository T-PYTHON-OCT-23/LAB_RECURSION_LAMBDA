def FizzBuzz_for():
    for n in range(1,100+1):
        if (n%3==0):
            print('Fizz')
        if (n%5==0):
            print("Buzz")
        if (n%3==0) and (n%5==0):
            print('FizzBuzz')

FizzBuzz_for()

print('_'*20)

def FizzBuzz_while():
    i=1
    while i<=100:
        if (i%3==0):
            print('Fizz')
        if (i%5==0):
            print("Buzz")
        if (i%3==0) and (i%5==0):
            print('FizzBuzz')
        i+=1

FizzBuzz_while()