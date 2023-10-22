def p(phrase:str):
    if len(phrase) ==0:
        return 0
    if phrase[0].lower()in"aeiou":
        return 1+ p(phrase[1:])
    else:
        return 0+ p(phrase[1:])   
    
print(p("I love python"))



numbers=[40,35, 10, 15, 20]
number_l= list(map(lambda x:x*x,numbers))
print(numbers)
print(number_l)