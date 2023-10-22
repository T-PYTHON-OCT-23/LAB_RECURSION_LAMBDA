num = [40,35, 10, 15, 20]
numbers = map(lambda x: x * x, num)
print(list(numbers))




def count_vowles(phrase) ->int:
    if len(phrase)== 0:
        return 0
    count = 0
    if phrase[0].lower() in "eaiou":
        count = 1
    return count + count_vowles(phrase[1:])
print(count_vowles("i love python"))
