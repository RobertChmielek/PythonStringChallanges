Way = "ay"
Word=input("Enter a word")
if Word[0] == "a" or Word[0] == "e" or Word[0] == "i" or Word[0] == "o" or Word[0] == "u":
    print(Word.lower()+"way")
else:
    WordLower = Word.lower()
    FirstLetter = WordLower[0]
    PigLatin = WordLower + FirstLetter + Way
    PigLatin = PigLatin[1:len(PigLatin)]
    print(PigLatin)