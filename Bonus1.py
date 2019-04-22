vowels = ["a", "e", "i", "o", "u"]
def pig_latin(word):
    word = word.lower()
    if word[0] not in vowels and word[1] in vowels:
        print(word[1:] + word[0] + "ay")
    elif word[0] not in vowels and word[1] not in vowels:
        print(word[2:] + word[:2] + "ay")
    elif word[0] in vowels:
        print((word.capitalize()) + "way")
    else:
        print("Unable to convert word to pig latin, sorry!")

pig_latin("happy")
pig_latin("child")
pig_latin("Awesome")