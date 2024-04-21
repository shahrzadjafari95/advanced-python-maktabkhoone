person_dict = {}
number_of_words = int(input('Enter number of words:'))
for i in range(number_of_words):
    words = list(map(str, input('Enter a word and its translations:').split()))
    person_dict[words[0]] = words[1:]

sentence = input('Enter sentence:')

for word in sentence.split():
    for key, value in person_dict.items():
        if word in value:
            sentence = sentence.replace(word, key)

print('The translated sentence:', sentence)
