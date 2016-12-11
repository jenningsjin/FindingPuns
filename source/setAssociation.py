import sys
import os
import re
import requests
import itertools

def printList(list):
    for item in list:
        print item

def getData(filename):
    fileObj = open(filename)
    textList = fileObj.read()
    textList = textList.split('\n\n')

    for i in xrange(len(textList)):
        textList[i] = textList[i].split('\n')
        # textList[i][0] = textList[i][0].split(' ')
        textList[i] = textList[i][0].split(' ')
    return textList


# Make the API call to google to figure out
# word the bigram score is
def checkAssocation(word1, word2):
    requestURL = "https://api.projectoxford.ai/text/weblm/v1.0/calculateJointProbability?model=body&order=2"
    authKey = "2a1f5273165e407a8b3981aa640eb565"
    headers = {"Ocp-Apim-Subscription-Key":authKey}
    # query = "{ \"queries\": [" + word1 + ' ' + word2 + "] }"
    query = """{{\"queries\": [\"{0} {1}\"] }}""".format(word1, word2)
    r = requests.post(requestURL, headers=headers, data=query)
    return r.json()['results'][0]['probability']




# Given the Sentence, get the scores for each bigram
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
    filename = "../data/puns.txt"
    dataList = getData(filename)

    sentence = "Hello it's me"
    print getSentenceScores("A dog gave birth to puppies near the road and was cited for littering.".split(' '))


