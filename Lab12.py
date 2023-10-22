#Q1)
def vowels_in_word (word:str):
    words = word.split()
    count = 0

    if len(word)==0:
        return 0
    elif word[0] in ['a','e','i','u','o','A','E','I','U','O']:
       count = count+1
    return count + vowels_in_word(word[1:])

result = vowels_in_word("I love python")
print("The number of vowls is : " , result)


print("-------------------")

#Q2)
number = [40,35, 10, 15, 20]
new_list = map(lambda i : i*i , number)
print(list(new_list))





