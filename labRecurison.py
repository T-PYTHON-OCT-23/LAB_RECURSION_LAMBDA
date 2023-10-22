#Q1
def vowelsLetter(phrase)-> int:
    
    #phrase = phrase[1:]
    count = 0
    if len(phrase) == 0:
        return count

    char =  phrase[0]

    if char in "aeuio":
        count = count +1
    
    return count+vowelsLetter(phrase[1:])
    


word = "I love python"

print(f"Number of vowels: {vowelsLetter(word.lower())}")


print("-"*20)

#Q2

numbers = [40, 35, 10, 15, 20]
multiplynumbers = list(map(lambda num: num * num, numbers))
   
print(f"Original list: {numbers}")
print(f"List after multiplying the numbers: {multiplynumbers}")


