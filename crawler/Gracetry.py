from lxml import html
import re
import requests





if __name__ == '__main__':

	# word = '1'
	# url = ''.join(['http://www.punoftheday.com/cgi-bin/disppuns.pl?ord=S&cat=4&sub=0401&page=', word])
	url = 'http://www.punoftheday.com/cgi-bin/disppuns.pl?ord=S&cat=4&sub=0401&page='
	

	punList = []
	for i in xrange(1,10):
		page = requests.get(url + str(i))
		tree = html.fromstring(page.text)
		htmlpage = html.tostring(tree)
		htmlpage = htmlpage.split("<!-- Puns -->")[1]
		htmlpage = htmlpage.split("<!-- google_ad_section")[0]
			

		for line in htmlpage.split("\n"):
			if '<div class="credit"' in line:
				line2 = line[line.index("<td>") + len("<td>"):line.index("<div class=")]
				punList.append(line2)
				print line2