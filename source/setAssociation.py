import sys
import os
import re
import json
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
    
    query = """{{\"queries\": [\"{0} {1}\"] }}""".format(word1, word2)
    r = requests.post(requestURL, headers=headers, data=query)
    return r.json()['results'][0]['probability']

#Makes API to Microsoft to figure out scores for an entire List of Bigram
def checkAssociationBatch(bigramList):
    requestURL = "https://api.projectoxford.ai/text/weblm/v1.0/calculateJointProbability?model=body&order=2"
    authKey = "2a1f5273165e407a8b3981aa640eb565"
    headers = {"Ocp-Apim-Subscription-Key":authKey}

    bigramStrings = [pair[0] + ' ' + pair[1] for pair in  bigramList]

    # query = """{{\"queries\": [\"{0} {1}\"] }}""".format(word1, word2)


    query = "{\"queries\":" + str(bigramStrings) + "}"  
    r = requests.post(requestURL, headers=headers, data=query)
    
    outputMap = {} 
    for data in r.json()['results']:
        words = data['words'].split(' ')
        word1 = words[0]
        word2 = words[1]

        pair = (str(word1), str(word2))
        if not outputMap.get(pair):
            outputMap[pair] = float(data['probability'])

    return outputMap
    # return r.json()['results'][0]['probability']    


# Given the Sentence, get the scores for each bigram
# in the sentence
def getSentenceScores(sentenceList):
    scoreMap = {}
    permutationList = list(itertools.permutations(sentenceList, 2))
    for bigram in permutationList:
        word1 = bigram[0]
        word2 = bigram[1]

        print word1 +  ' | ' + word2
    #     score = checkAssocation(word1, word2)
    #     bigram = (word1, word2)

    #     if not scoreMap.get(bigram):
    #         scoreMap[bigram] = score
    # return scoreMap



# Find the Word that appears in the highest number of 
# high scoring sets
def setCompare(scores):
    return



if __name__ == "__main__":
    filename = "../data/puns.txt"
    dataList = getData(filename)

    sentence = "Hello it's me"
    # print getSentenceScores("A dog gave birth to puppies near the road and was cited for littering.".split(' '))
    # print getSentenceScores("A dog gave bircth to puppies".split(' '))
    listo = [('A', 'dog'), ('A', 'gave'), ('A', 'birth'), ('A', 'to'), ('A', 'puppies'), ('A', 'near'), ('A', 'the')]

    print checkAssociationBatch(listo)
