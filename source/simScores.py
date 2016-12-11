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
		senseweight = 0

		for ss in senses[token]:

			for othertoken in line:
				if token != othertoken:
					for otherss in senses[othertoken]:
						senseweight += max(0, ss.path_similarity(otherss))

			tokensenses.append(senseweight)
			senseweight = 0

		weight = analyzesenses(tokensenses)
		wordweights.append(analyzesenses(tokensenses))
						# print token + ", " + othertoken
						# print max(0, ss.path_similarity(otherss))
						

		# if len(senses[token]) > 0:
		# 	weight = float(weight)/len(senses[token])
		# wordweights.append(weight)
		tot += weight

	return normalize(wordweights, tot)




# if __name__ == '__main__':
# 	sents = [ ['rocky', 'rough', 'rock'],
# 			  ['horse', 'stable', 'animal'],
# 			  ['deer', 'buck', 'teeth'],
# 			  ['duck', 'bartender', 'bill']
# 			]

# 	for line in sents:
# 		print line
# 		print simscores(line)



# synsets = {}
# tokenTopScores = {}
# for token in tokens:
# 	# get the list of senses of that word
#     synsets[token] = wordnet.synsets(token)
#     tokenTopScores[token] = {}

# # for every word in that sentence
# for token in tokens:
# 	# for every sense for that word
#     for synset in synsets[token]:

#         tokenTopScores[token][synset] = 0

#         #for the rest of the words in that sentence
#         for otherToken in tokens:
#         	# skip if same word
#             if token == otherToken:
#                 continue
#             maxScore = 0

#             # finds the most 
#             for otherSynset in synsets[otherToken]:
#                 maxScore = max(maxScore, synset.path_similarity(otherSynset))
#             tokenTopScores[token][synset] += maxScore

# for token in tokens:
#     print(token)
#     currentMax = 0
#     for synset in synsets[token]:
#         if tokenTopScores[token][synset] > currentMax:
#             print(synset.definition(), tokenTopScores[token][synset])
#         currentMax = max(currentMax, tokenTopScores[token][synset])
#     print('')