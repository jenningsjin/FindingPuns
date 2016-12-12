from nltk.corpus import wordnet
from stop_words import get_stop_words
import re

def normalize(weights, tot):
	normweights = []
	if tot == 0:
		return weights

	for num in weights:
		normweights.append(float(num)/tot)
	return normweights

# given a list of scores for every sense of a word
# returns the probability/weight that the word in reference
# is a pun word
def analyzesenses(senses):
	# must have at least two senses
	length = len(senses)
	if length < 2:
		return 0
	if length == 2:
		return max(senses[0], senses[1]) - abs(senses[0] - senses[1])

	one = 0
	two = 0
	three = 0

	for s in senses:
		if s > one:
			three = two
			two = one
			one = s 
		elif s > two:
			three = two
			two = s
		elif s > three:
			three = s

	return float((one - three) + (two - three))/2

def simScores(line):
	linelen = len(line)
	tot = 0
	tokens = []
	senses = {}
	sensesum = {}
	for token in line:
		senses[token] = wordnet.synsets(token)

	wordweights = []
	for token in line:
		tokensenses = []
		weight = 0

		for ss in senses[token]:

			for othertoken in line:
				if token != othertoken:
					for otherss in senses[othertoken]:
						weight += max(0, ss.path_similarity(otherss))

		# 	tokensenses.append(senseweight)
		# 	senseweight = 0

		# weight = analyzesenses(tokensenses)
		# wordweights.append(analyzesenses(tokensenses))
						# print token + ", " + othertoken
						# print max(0, ss.path_similarity(otherss))
						

		if len(senses[token]) > 0:
			weight = float(weight)/len(senses[token])
		wordweights.append(weight)
		tot += weight
	#print normalize(wordweights, tot)
	return normalize(wordweights, tot)
	