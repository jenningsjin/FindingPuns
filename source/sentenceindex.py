import math


def normalize(weights, tot):
	normweights = []
	for num in weights:
		normweights.append(float(num)/tot)
	return normweights

# given a list of sentences, which are represented as lists
def sentenceIndex(line):
	wordweights = []
	linelen = len(line)
	tot = 0

	for ind, word in enumerate(line):
		# holds the sum of all weights
		tot += math.pow(2, ind)
		wordweights.append(math.pow(2, ind))

	return normalize(wordweights, tot)

# if __name__ == '__main__':
# 	test = [['word', 'is', 'funny', 'lol'],
# 			['I', 'am', 'very', 'busy', 'every', 'day']
# 			]
# 	print sentenceindex(test)