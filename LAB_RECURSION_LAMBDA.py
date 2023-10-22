def many_vowels(phrase)->int:
    count=0 
    if len(phrase)==0:
        return count
    if phrase[0] in "aeiou":
        count+=1
    return count+many_vowels(phrase[1:])

phrase="I love python"
print(f"number vowels in {many_vowels(phrase.lower())}")




# 2) create a new list containing each number from the previous list mutliplied by itself
result= map(lambda n :n*n, [40,35, 10, 15, 20])
print(list(result))