def reverse(sentence):

    words = sentence.split()

    words_reversed = words[::-1]
    reversed = ' '.join(words_reversed)
    return reversed

user_input = input("Enter a sentence: ")
reversed_sentence = reverse(user_input)
print(reversed_sentence)
