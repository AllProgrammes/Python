def shortner(sentance, word):
    edited = sentance.replace(word, "")
    edited = edited.strip()
    return edited.replace("  ", " ")


sentance = input("Enter your paragraph or sentance here : ")
word = input("Enter the word which you want to remove : ")
print(shortner(sentance, word))
