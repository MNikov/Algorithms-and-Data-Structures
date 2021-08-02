# Anagram problem overview
# Interview Question #4
# Construct an algorithm to check whether two words (or phrases) are anagrams or not!
# "An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, " \
# "typically using all the original letters exactly once"
# For example: restful and fluster

def anagram_checker_1(word1, word2):
    return sorted(word1) == sorted(word2)


# Course implementation
def anagram_checker_2(word1, word2):
    if len(word1) != len(word2):
        return False
    word1 = sorted(word1)
    word2 = sorted(word2)

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            return False
    return True


print(anagram_checker_1('stop', 'post'))
print(anagram_checker_2('mug', 'gum'))
print(anagram_checker_1('spell', 'spill'))
print(anagram_checker_2('run', 'ran'))
print(anagram_checker_2('weight', 'weigh'))
