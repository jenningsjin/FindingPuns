from lxml import html
import re
import requests





if __name__ == '__main__':

	word = '1'
	url = ''.join(['http://www.punoftheday.com/cgi-bin/disppuns.pl?ord=S&cat=4&sub=0401&page=', word])
	page = requests.get(url)
	tree = html.fromstring(page.text)

	htmlpage = html.tostring(tree)
	htmlpage = htmlpage.split("<!-- Puns -->")[1]
	htmlpage = htmlpage.split("<!-- google_ad_section")[0]


	for line in htmlpage.split("\n"):
		if '<div class="credit"' in line:
			line2 = line[line.index("<td>") + len("<td>"):line.index("<div class=")]
			print line2