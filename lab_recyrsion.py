
#Recursion

def count_vowels(text:str) ->int:
    count = 0


    if len (text) == 0:
        return 0
    
    # Check (a,e,i,o,u)

    if text[0].lower() in "aeiou":
        return 1 + count_vowels(text[1:])  # # يتضمن حرف العلة هذا والتكرار في بقية النص
    else:
        return 0 + count_vowels(text[1:])  # استمرار في تحقق 


# Test the function 
text_input=input("text :")
count =count_vowels(text_input)
print(f" the vowels {text_input} is  {count}")




## 2) Given a list of numbers : `[40,35, 10, 15, 20]`

list_of_numbers = [40, 35, 10, 15, 20]

multiply_numbers = list(map(lambda x: x * x, list_of_numbers))

print(list(multiply_numbers))


