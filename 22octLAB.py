#----------------Q1------------------
def voulesCounter(sentence:str)->int:
    if len(sentence)==0 :
        return 0
    elif sentence[0].lower()=="a" or sentence[0].lower()=="e" or sentence[0].lower()=="i" or sentence[0].lower()=="o" or sentence[0].lower()=="u":
        return 1 + voulesCounter(sentence[1:])
    else:
        return 0 + voulesCounter(sentence[1:])
test ="I love python"
print(voulesCounter(test))
#----------------Q2-----------------
my_list=[40,35, 10, 15, 20]
my_new_list= list(map(lambda num: num*num, my_list))
print(my_new_list)