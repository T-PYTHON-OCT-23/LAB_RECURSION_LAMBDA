

def count_vowels(x):
    if len(x) == 0:
        return 0
    char = x[0]
    if char in "aeiou":
        return 1 + count_vowels(x[1:])
    else:
        return 0 + count_vowels(x[1:])

x = "i love python"
print(count_vowels(x))




def square(x):
    return x * x

numbers =[40 , 35, 10, 15,20]

squared_numbers = list(map(square, numbers))

print(squared_numbers)