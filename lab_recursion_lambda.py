def count_vowels (phrase:str)->int:
    if len(phrase) == 0 :
        return 0
    count = 0 
    if phrase[0].lower() in "eaiuo":
        count = 1 
        
    return count + count_vowels(phrase[1:])
 


phrase ="I love python"
print(count_vowels(phrase))

print("---- LAMBDA----")
numbres = [40,35, 10, 15, 20]
mutliplied_numbres = map(lambda num : num * num ,numbres )
print(list(mutliplied_numbres))




