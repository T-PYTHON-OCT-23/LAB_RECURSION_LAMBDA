vowels=("a","e","i","o","u")
def countVowels(phrase):
    if phrase == "":
        return 0
    if phrase[0].lower() in vowels:
        return 1 + countVowels(str(phrase[1:]))
    else:
        return countVowels(str(phrase[1:]))

print("number of vowels in your pharse",countVowels("I love python"))
list_=[40,35, 10, 15, 20]
square=lambda x: x**2
timesTwo=list(map(square,list_))
print(timesTwo)