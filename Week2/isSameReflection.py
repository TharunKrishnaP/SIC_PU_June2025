def isSameReflection(word1,word2):
    if len(word1) != len(word2):
        return -1
    else:
        temp = word2 * 2
        if temp.find(word1) != 0:
            return 1
        else:
            return -1

word1 = input(("Word 1 = ")).lower()
word2 = input(("Word 2 = ")).lower()
result = isSameReflection(word1,word2)
print(result)