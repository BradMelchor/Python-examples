#!/usr/bin/env python3
def pig_latin(word):
    if word[0] in "aeiouy":
        return word + 'way'
    else:
        words = findvowel(word)
        if words >= 1:
            word = (word[words:] + word[:words] + 'ay')
            return word
        else:
            word = (word[words:] + word[:words] + 'ay')
            return word

def findvowel(word):
    for i in range(len(word)):
        if checkvowel(word[i]) == True:
            return i
    
def checkvowel(char):
    vowel = "aeiouy"
    for vowels in vowel:
        if char == vowels:
            return True
    return False

def main():
    print("Pig Latin Translator")
    print()
    print()

    choice = "y"
    while choice.lower() == "y":
        words = input("Enter Text: ").strip()
        words = words.lower()
        words = str(words)
        if "." in words:
            words = words.replace("." , "")
        if "'" in words:
            words = words.replace("'", "")
        if "!" in words:
            words = words.replace("!", "")
        if "?" in words:
            words = words.replace("?", "")
        print("English: " + words)
        print("Pig Latin: "+ ' '.join(pig_latin(word) for word in words.split()))


if __name__ == "__main__":
    main()
