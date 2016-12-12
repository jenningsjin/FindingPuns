from nltk.corpus import wordnet
from stop_words import get_stop_words
import numpy as np
import re

wordBags = {}
pattern = '\(|\)|\.|,| |\?|\!|\:|\;|\''
stopWords = get_stop_words('en')
def bagOfWordsSimilarityScore(tokens, synsets):
    # generate a bag of words for every token
    for token in tokens:
        if token in wordBags:
            continue
        wordBags[token] = []
        for synset in synsets[token]:
            words = re.split(pattern, synset.definition().lower())
            # TODO: add in synset.examples()
            words = [word for word in words if word and word not in stopWords]
            wordBags[token].extend(words)
    return scoreTokenSenses(tokens, synsets)

def scoreTokenSenses(tokens, synsets):
    scores = []
    # for every sense of every token
    for token in tokens:
        scoresPerSense = []
        for synset in synsets[token]:
            currentTokenBag = re.split(pattern, synset.definition().lower())
            currentTokenBag = [word for word in currentTokenBag if word and word not in stopWords]
            senseScore = 0
            # compare to bag of words of other tokens
            for otherToken in tokens:
                if token == otherToken:
                    continue
                wordBag = wordBags[token]
                for word in currentTokenBag:
                    if word in wordBag:
                        senseScore += 1
            scoresPerSense.append(senseScore)
        npScores = np.array(scoresPerSense)
        # sort high to low
        npScores[::-1].sort()
        if len(npScores) > 2:
            # favor close #1 and #2 and far #2 and #3
            scores.append(1-(npScores[0]-npScores[1])/float(npScores[0]) + (npScores[1]-npScores[2])/float(npScores[1]))
        elif len(npScores) == 2:
            # favor close #1 and #2
            scores.append(1-(npScores[0]-npScores[1])/float(npScores[0]))
        else:
            # TODO check this for a reasonable value
            scores.append(0.3)
    s = np.array(scores)
    s = s / np.sum(s)
    return s.tolist()
