def recursion_vowels (vowels) ->str:
    vowels_letter ="aeiouAEIOU"
    count = 0
    if  len(vowels) == 0 :
     return 0     
    if vowels[0] in vowels_letter:
      return 1 + recursion_vowels(vowels[1:])
    else:
      return 0 + recursion_vowels(vowels[1:])
              
  
words = input("enter the word/s : ")
count=recursion_vowels(words)
result =print(f" the vowels in {words} is {count}")



print()

list_number= [40,35, 10, 15, 20]

multiply_numbers = map (lambda item : item*item , list_number )

print(list(multiply_numbers))

 
        






                 


       