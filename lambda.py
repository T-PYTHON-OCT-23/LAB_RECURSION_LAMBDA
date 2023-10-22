# 1
def count_vowels(phrase: str):
    if len(phrase) == 0:
        return 0

    count = 0
    if phrase[0].lower() in "ioeuaIOEUA":
        count = 1

    return count + count_vowels(phrase[1:])


# 2
numbers = [40, 35, 10, 15, 20]
numbers_multiplied = map(lambda numbers: numbers*numbers, numbers)
print(numbers_multiplied)
