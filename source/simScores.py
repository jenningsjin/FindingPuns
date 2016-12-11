from nltk.corpus import wordnet
from stop_words import get_stop_words
import re

def normalize(weights, tot):
	normweights = []
	for num in weights:
		normweights.append(float(num)/tot)
	return normweights

def simweights(tokens):
	tokens = []
	for word in line:
		# only consider tokens that have more than two senses
		if len(wordnet.synsets(word)) >= 2:
			tokens.append(word)

	wordweights = []




def simscores(sentences):
	allweights = []

	for line in sentences:
		wordweights = []
		linelen = len(line)
		tot = 0

		wordweights = simweights(line)






synsets = {}
tokenTopScores = {}
for token in tokens:
	# get the list of senses of that word
    synsets[token] = wordnet.synsets(token)
    tokenTopScores[token] = {}

# for every word in that sentence
for token in tokens:
	# for every sense for that word
    for synset in synsets[token]:

        tokenTopScores[token][synset] = 0

        #for the rest of the words in that sentence
        for otherToken in tokens:
        	# skip if same word
            if token == otherToken:
                continue
            maxScore = 0

            # finds the most 
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





