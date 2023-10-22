
vowels=['a','i','o','u','e']
def vowels_letters(string:str)->int:
    if len(string)==0:
        return 0
    count = 0
    if string[0].lower() in vowels:
        count=1
        return count + vowels_letters(string[1:])

value = input("Enter a sentence: ")
print(vowels_letters(value))