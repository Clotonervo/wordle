# -*- coding: utf-8 -*-
import string

from trie import TrieNode

lettersToKeep = []


# ________________________________ Optimized functions
def optimizeList(wordList):
    # Each word gets a score based on other words in the dictionary
    # Letters in same word get +1
    # Letters in same position get +2 (greens are better than yellows)
    # Then sort based on values/return highest value

    valueList = []

    if wordList == []:
        return "No word found"

    for word in wordList:
        value = 0

        for x in range(0, len(word)):
            letter = word[x]
            for i in range(0, len(wordList)):
                compareWord = wordList[i]
                if compareWord == word:
                    continue
                elif letter in compareWord and letter == compareWord[x]:
                    value += 2
                elif letter in compareWord:
                    value += 1

        valueList.append(value)
    max_value = max(valueList)
    max_index = valueList.index(max_value)

    return wordList[max_index]


def optimizeBiggestPartition(wordList):
    # Returns word based on biggest difference in wordList

    # PROBLEM: How to I account for the different posibilities of the guess results? Do I try ever permuitation of guess results?
    # for word in wordList:
    return


def optimizeTrie(wordList):
    # Returns the best word based on trie data structure
    trie = createTrie(wordList)
    word = ""
    while(not trie.word_finished):
        max_value = max(trie.children)
        trie = trie.children[trie.children.index(max_value)]
        word = "".join((word, trie.char))

    return word


def createTrie(wordList):
    #Creates trie stucture based on word list
    head = TrieNode('*')

    for word in wordList:
        head.add(head, word)

    return head

# _________________________________ Partition functions
def removeGreys(letter, wordList):
    # Remove all words that have grey letters
    tempWordList = []

    for word in wordList:
        if letter not in word or letter in lettersToKeep:
            tempWordList.append(word)

    return tempWordList


def removeYellows(letter, position, wordList):
    # Remove all yellow letters at the same position
    tempWordList = []
    lettersToKeep.append(letter)

    for word in wordList:
        if letter in word and word[position] != letter:
            tempWordList.append(word)

    return tempWordList


def removeAllNonGreens(letter, position, wordList):
    # Remove all words that don't have a green letter in their position
    tempWordList = []
    lettersToKeep.append(letter)

    for word in wordList:
        if word[position] == letter:
            tempWordList.append(word)

    return tempWordList


def partitionWords(guess, result, wordList):
    for i in range(0, len(result)):
        if result[i] == "X":
            wordList = removeGreys(guess[i], wordList)
        elif result[i] == "Y":
            wordList = removeYellows(guess[i], i, wordList)
        else:
            wordList = removeAllNonGreens(guess[i], i, wordList)

    return wordList


# ______________________________ Main wordle function
def startWordle(wordList):
    counter = 0
    while (True):
        if (wordList == []):
            print("Invalid combination. Better luck next time!")
            return

        guess = raw_input("Your guess:\n")
        result = raw_input("Your result: (G is green, Y is yellow, and X is grey)\n")
        counter += 1
        listSize = len(wordList)

        if result == "GGGGG":
            print("Good job!\n")
            print("Solved in " + str(counter) + " guesses\n")
            return
        else:
            wordList = partitionWords(guess, result, wordList)
            print("Removed " + str(listSize - len(wordList)) + " answers\n")
            print("Next guess:\n")
            print(optimizeList(wordList))
            print("Trie word: " + optimizeTrie(wordList))
            print(wordList)


if __name__ == '__main__':
    print("Test")

    my_file = open("wordle-answers-alphabetical.txt", "r")
    content = my_file.read().splitlines()
    startWordle(content)
