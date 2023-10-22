


word=(" I love python")
def num_of_vowels(word):
    w = word.split()
    count=0
    if len(word)==0:
        return 0
    elif word[0]=="i" or word[0]=="a" or word[0]=="e" or word[0]=="o" or word[0]=="u" or word[0] == "A" or word[0]=="I" or word[:]=="E" or word[0]=="O" or word[0]=="U":
        count+=1

    return count + num_of_vowels(word[1:])
        




print(" the vowels number is : ")
print(num_of_vowels(word))



#--------------------------


numbers=[40,35, 10, 15, 20]
new_numbers= map (lambda i: i*i , numbers)
print("the new list of multiply each number by itself: ")
print(list(new_numbers))
