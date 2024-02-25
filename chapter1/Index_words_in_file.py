# def get_sentence():
#     input_sentence = input('enter your sentence:').split('.')
#     print(input_sentence)
#     counter = 1
#     all_words = []
#     for word in input_sentence[1:]:
#         counter += 1
#         word_and_index = []
#         if word.istitle():
#             word = word.strip('.')
#             word = word.strip(',')
#             word_and_index.append(word)
#             word_and_index.append(counter)
#             all_words.append(word_and_index)
#
#     return all_words


# print(get_sentence())

#
import re

inp = input()
sentences = re.findall(r"[\w\s,]*[\.\!\?]", inp)
counter = 0
for sentence in sentences:
    sentence = re.sub(r"\W", " ", sentence)
    sentence = re.sub(r"\s+", " ", sentence)
    words = re.split(r"\s", sentence)
    words = [w for w in words if w != ""]
    for i, word in enumerate(words):
        if word != "" and i != 0:
            if re.search(r"[A-Z]+", word):
                print("%d:%s" % (counter + i + 1, word))

    counter += len(words)

