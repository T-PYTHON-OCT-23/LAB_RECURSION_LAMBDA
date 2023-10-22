def count_vowels(word):
  vowels = ['a', 'e', 'i', 'o', 'u']

  if word == "":
    return 0

  if word[0].lower() in vowels:
    return 1 + count_vowels(word[1:])
  else:
    return count_vowels(word[1:])

print(count_vowels("I love python"))

list1=[40,35, 10, 15, 20]
list_mutliplied=lambda x:x*x
print(list(map(list_mutliplied,list1)))