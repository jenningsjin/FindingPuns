import sys
import urllib2

seedURLs = ""

if __name__ == "__main__":
	seedURL = sys.argv[1]

	baseLink = seedURL

	# Process Seed URL
	baseLink = baseLink[:-1]

	punList = []
	#get the first 10 pages of puns
	for i in xrange(1, 10):
		htmlpage = urllib2.urlopen(baseLink + str(i))
		# print page.read()
		htmlpage = htmlpage.split("<!-- Puns -->")[1]
		htmlpage = htmlpage.split("<!-- google_ad_section")[0]


		for line in htmlpage.split("\n"):
			if '<div class="credit"' in line:
				line2 = line[line.index("<td>") + len("<td>"):line.index("<div class=")]
				print line2




