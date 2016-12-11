# Team: Radata
# 	Jennings Jin
# 	Justin Kim
# 	Ian Lin
# 	Grace Wu
import sys
from nltk.corpus import wordnet as wn

class FindPuns:
	def __init__(self, filename):
		self.correct = []
		self.guesses = []
		self.stopwords = ['a','all','an','and','any','are','as','at','be','been','but','by ','few','from','for','have','he','her','here','him','his','how','i','in','is','it','its','many','me','my','none','of','on ','or','our','she','some','the','their','them','there','they','that ','this','to','us','was','what','when','where','which','who','why','will','with','you','your']

		# self.sentenceindex(filename)

		self.wordnet(filename)




	def wordnet(filename):
		print "something works"




	# def sentenceindex(self, filename):
	# 	tri = 0
	# 	with open(filename) as f:
	# 		sentence = []
	# 		word = ""
	# 		correct = 0
	# 		total = 0
	# 		for line in f:
	# 			if tri == 0:
	# 				line = line[:len(line)-1]
	# 				sentence = self.processline(line.split(" "))
	# 			elif tri == 1:
	# 				line = line[:len(line)-1]
	# 				if line == sentence[len(sentence)-1]:
	# 					correct += 1
	# 				total += 1
	# 			elif tri == 2:
	# 				tri = -1
	# 			tri += 1

	# 		print "Total: " + str(total)
	# 		print "Correct: " + str(correct)
	# 		print "Percentage accuracy: " + str(float(correct)/total)

	def processline(self, sentencelist):
		sentencereturn = []
		for word in sentencelist:
			if word not in self.stopwords:
				sentencereturn.append(self.process(word))
		return sentencereturn

	def process(self, word):
		for char in word:
			if char in "\"?!.(),:;'":
				word = word.replace(char, '')
		return word.lower()

if __name__ == "__main__":
	trainfile = sys.argv[1]
	FindPuns(trainfile)
