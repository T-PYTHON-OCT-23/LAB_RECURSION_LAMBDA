


def count_vowels(phrase):

    if len(phrase)==0:
        return 0
    
    if phrase[0].lower() in "aeiou":
        return 1 + count_vowels(phrase[1:])
    else: return 0 + count_vowels(phrase[1:])



ss=count_vowels("I love python")
print(ss)




print('-'*20)

numbers=[40,35, 10, 15, 20]

mult_numbers=map(lambda number:number*number,numbers )

new_list=list(mult_numbers)


print(new_list)