def count_vowels(word):
    word = word.lower()  
    if word == "":
        return 0 
    elif word[0] in "aeiou":
        return 1 + count_vowels(word[1:])  
    else:
        return count_vowels(word[1:])  

print(count_vowels("I love python"))  

num = [40,35, 10, 15, 20]
num_power = map(lambda item: item**2,num)
print(list(num_power))