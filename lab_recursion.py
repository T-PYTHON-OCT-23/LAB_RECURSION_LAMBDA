def vowels_letters(string:int)->int:
    count=0
    vowels={'a','i','o','u','e'}
    for i in string:
        if i in vowels:
            count +=1
            return count


value = input("Enter a sentence: ")
print(vowels_letters(value))