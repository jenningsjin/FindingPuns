from nltk.corpus import wordnet
import requests
from random import randint

def ngramsOfSynonymsSimilarityScore(tokens):
	ngramsScores = createNgramsScoreMap(tokens)

	ambiguityScores = []
	for token in tokens:
		senses = wordnet.synsets(token)
		senses = [sense for sense in senses if len(sense.lemma_names()) >= 2]

		senseScores = []
		for sense in senses:

			associationScore = 0.0
			synonyms = sense.lemma_names()[1:]

			for synonym in synonyms:
				synonym = synonym.replace("_", " ")
				synonym = synonym.lower()
				for word in tokens:
					ngram = token + " " + synonym
					associationScore += ngramsScores[token + " " + synonym]

			associationScore = associationScore / len(synonyms) / len(tokens)
			senseScores.append(associationScore)

		senseScores = sorted(senseScores, reverse = True)
		senseScores = [abs(1.0 / score) for score in senseScores]
		if len(senseScores) > 2:
			ambiguityScores.append(1-(senseScores[0]-senseScores[1])/float(senseScores[0]) + (senseScores[1]-senseScores[2])/float(senseScores[1]))
		elif len(senseScores) == 2:
			ambiguityScores.append(1-(senseScores[0]-senseScores[1])/float(senseScores[0]))
		else:
			ambiguityScores.append(0.3)

	ambiguityScores = normalize(ambiguityScores)
	return ambiguityScores

def normalize(scores):
	total = sum(scores)
	if total == 0:
		return scores
	else:
		return [1.0 * score/total for score in scores]
    
def createNgramsScoreMap(tokens):
	# create all possible ngrams
	synonyms = set()
	ngramsSet = set()

	for token in tokens:
		senses = wordnet.synsets(token)
		senses = [sense for sense in senses]

		for sense in senses:
			for synonym in sense.lemma_names():
				synonyms.add(synonym.replace("_", " "))

	for token in tokens:
		for synonym in synonyms:
			ngram = token + " " + synonym
			ngramsSet.add(ngram)

	# query those ngrams for probability scores
	return queryBatchNgramsScores(ngramsSet)

def queryBatchNgramsScores(ngramsSet):

	requestURL = "https://api.projectoxford.ai/text/weblm/v1.0/calculateJointProbability?model=body&order=2"
	authKey = "2a1f5273165e407a8b3981aa640eb565"
	headers = {"Ocp-Apim-Subscription-Key":authKey}

	bigramStrings = [str(ngram) for ngram in ngramsSet]
	
	ngramsScores = {}
	i = 0
	while (i < len(bigramStrings)):
		if (len(bigramStrings) - i <= 1000):
			batch = bigramStrings[i:]
		else:
			batch = bigramStrings[i:i+1000]
		i += 1000

		query = "{\"queries\":" + str(batch) + "}" 
		r = requests.post(requestURL, headers=headers, data=query)

		for data in r.json()['results']:
			ngram = data['words']
			if ngram not in ngramsScores:
				ngramsScores[ngram] = float(data['probability'])

	return ngramsScores
