# Team: Radata
# 	Jennings Jin
# 	Justin Kim
# 	Ian Lin
# 	Grace Wu
# This is the main driver, only put driver related code here
import sys
import re
from stop_words import get_stop_words
from nltk.corpus import wordnet
import numpy as np
from sentenceindex import sentenceIndex
from simScores import simScores
from bagOfWordsSimilarity import bagOfWordsSimilarityScore
from ngramsOfSynonyms import ngramsOfSynonymsSimilarityScore

# constants
pathToPuns = '../data/puns.txt'
pathToShortPuns = '../data/shortPuns.txt'
stopWords = get_stop_words('en')
class FindPuns:
	def __init__(self):
		# full pun
		self.input = []
		# tokenized input
		self.x = []
		# output, list of predicted pun words
		self.y = []
		# same shape as x, every token of every pun will have a score
		self.scores = []
		# weights for the scores
		self.W = []
		# synsets
		self.synsets = {}

	def readInput(self):
		# format of file repeats every 3 lines
		# 1. pun 2. pun word 3. blank line
		with open(pathToPuns) as f:
			for line in f.read().splitlines():
				# ignore blank lines
				if not line:
					continue
				# pun
				if ' ' in line:
					self.input.append(line)
					self.x.append(self.tokenize(line))
				# pun word
				else:
					self.y.append(line)

	# lowercases, splits on spaces and punctuation, and removes stopword
	def tokenize(self, context):
		# split on spaces, commas, ?, !, :, ;, ',
		# update as necessary
		pattern = '\.|,| |\?|\!|\:|\;|\''
		tokens = re.split(pattern, context.lower())
		for token in tokens:
			# already looked it up
			if token in self.synsets:
				continue
			synset = wordnet.synsets(token)
			if len(token) > 1 and synset:
				self.synsets[token] = synset
		return [token for token in tokens if token not in stopWords and token in self.synsets]

	def findPuns(self):
		self.predictions = []
		for tokens in self.x:
			scores = []
			scores.append(simScores(tokens))
			scores.append(bagOfWordsSimilarityScore(tokens, self.synsets))
			#scores.append(ngramsOfSynonymsSimilarityScore(tokens))
			#scores.append(jenningsScoreFunction(tokens))
			scores.append(sentenceIndex(tokens))
			scores = self.squashAndNormalizeScores(scores)
			self.predictions.append(tokens[np.argmax(scores)])
		totalCount = 0
		wrongCount = 0
		for p, target in zip(self.predictions, self.y):
			totalCount += 1
			if p != target:
				wrongCount += 1
		print('total count is ' + str(totalCount) + ' wrong ' + str(wrongCount))

	# scores is a 2d vector, each row contains scores from a separate scoring function
	def squashAndNormalizeScores(self, scores):
		# TODO: for now, we simply weight the scores evenly (just sum up rows)
		return np.sum(np.atleast_2d(scores), axis=0, keepdims=True)

if __name__ == "__main__":
	findpuns = FindPuns()
	findpuns.readInput()
	findpuns.findPuns()
