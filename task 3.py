def maximum_length_string(sentence):
    words=sentence.split()
    max_word=""
    for i in words:
        if len(i)>len(max_word):
            max_word=i
    return max_word,len(max_word)
sentence=input("Enter a Sentence:")
word,length=maximum_length_string(sentence)
print(f"The maximum length of the word in the string is {word} and the length of the word is {length}")