import sys
import os
import re


# Make the API call to google to figure out
# word the bigram score is
def checkAssocation(word1, word2):
    score = 0.0
    return score


# Given the Setence, get the scores for each bigram
# in the sentence
def getSentenceScores(sentenceList):
    scoreMap = {}
    for i in xrange(len(sentenceList)-1):
        word1 = sentenceList[i]
        word2 = sentenceList[i+1]
        score = checkAssocation(word1, word2)
        bigram = (word1, word2)

        if not scoreMap.get(bigram):
            scoreMap[bigram] = score
    return scoreMap

# Find the Word that appears in the highest number of 
# high scoring sets
def setCompare(Scores):
    return

def processData(filename):
    return


def setCompareFeature(data):
    for sentence in text:
        print "hello"
    return

if __name__ == "__main__":
    print "Cheese"
