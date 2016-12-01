import sys
import urllib2

seedURLs = ""

if __name__ == "__main__":
	seedURL = sys.argv[1]

	baseLink = seedURL

	# Process Seed URL
	baseLink = baseLink[:-1]

	#get the first 10 pages of puns
	for i in xrange(1, 10):
		page = urllib2.urlopen(baseLink + str(i))
		print page.read()
		break

