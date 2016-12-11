from nltk.corpus import wordnet
from stop_words import get_stop_words
import re

def bagOfWordsSimilarityScore(self, tokens):
    
synsets = {}
tokenTopScores = {}
for token in tokens:
    synsets[token] = wordnet.synsets(token)
    tokenTopScores[token] = {}

for token in tokens:
    for synset in synsets[token]:
        tokenTopScores[token][synset] = 0
        for otherToken in tokens:
            if token == otherToken:
                continue
            maxScore = 0
            for otherSynset in synsets[otherToken]:
                maxScore = max(maxScore, synset.path_similarity(otherSynset))
            tokenTopScores[token][synset] += maxScore

for token in tokens:
    print(token)
    currentMax = 0
    for synset in synsets[token]:
        if tokenTopScores[token][synset] > currentMax:
            print(synset.definition(), tokenTopScores[token][synset])
        currentMax = max(currentMax, tokenTopScores[token][synset])
    print('')
