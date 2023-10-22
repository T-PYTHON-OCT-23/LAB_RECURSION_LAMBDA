
#Q1

def recursion_word(word:str) -> int:
    counter = 0
    if len(word) == 0:
        return counter
    x = word.lower()
    for phrase in x:
        if phrase == "i" or phrase == "a" or phrase == "u" or phrase == "e" or phrase == "o":
            counter += 1
            print(phrase)
    return counter + recursion_word(word.removeprefix(word))



x = recursion_word("I love python")
print(x)

numbers = [40,35,10,15,20]

print(numbers)

number_multi = map(lambda number: number**2,numbers)
print(list(number_multi))