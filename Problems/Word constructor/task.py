word_1, word_2 = input(), input()

result = ""

for letter_1, letter_2 in zip(word_1, word_2):
    result += f"{letter_1}{letter_2}"

print(result)