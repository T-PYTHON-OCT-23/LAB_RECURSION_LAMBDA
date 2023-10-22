vowels=("a","e","i","o","u")
def countVowels(phrase):
    count=0
    if phrase == "":
        return count
    phrase.split()
    tempChar=phrase[0]
    if tempChar.lower() in vowels:
        count+=1
    return count + countVowels(str(phrase[1:]))

print("number of vowels in your pharse",countVowels("I love python"))
    
list_=[40,35, 10, 15, 20]
square=lambda x: x*2
timesTwo=list(map(square,list_))
print(timesTwo)