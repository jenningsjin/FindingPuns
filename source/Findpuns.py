# Team: Radata
# 	Jennings Jin
# 	Justin Kim
# 	Ian Lin
# 	Grace Wu
import sys

class FindPuns:
	def __init__(self, filename):
		self.sentenceindex(filename)

	def sentenceindex(self, filename):
		tri = 0
		with open(filename) as f:
			sentence = []
			word = ""
			correct = 0
			total = 0
			for line in f:
				if tri == 0:
					line = line[:len(line)-1]
					sentence = self.processline(line.split(" "))
				elif tri == 1:
					line = line[:len(line)-1]
					if line == sentence[len(sentence)-1]:
						correct += 1
					total += 1
				elif tri == 2:
					tri = -1
				tri += 1

			print "Total: " + str(total)
			print "Correct: " + str(correct)
			print "Percentage accuracy: " + str(float(correct)/total)

	def processline(self, sentencelist):
		sentencereturn = []
		for word in sentencelist:
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