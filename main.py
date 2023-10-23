# LAB_RECURSION_LAMBDA
def findVowels(word, count=0):
    if word:
        if word[0] in ('A','E','I','O','U','a','e','i','o','u'):
            count += 1
        return findVowels(word=word[1:], count=count)
    else:
        return count
word = input("given the phrase :")
print(findVowels(word))

print("*"*15)

numbers = [4, 5, 2, 10, 7, 9, 12]

myNew_list=list(map(lambda x: x**2,numbers))

print(myNew_list)

