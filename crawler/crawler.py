from lxml import html
import re
import requests

if __name__ == '__main__':

	urlhalf = "http://www.punoftheday.com/cgi-bin/disppuns.pl?ord=S&cat="
	urlotherhalf = "&page="
	validcats = ['4&sub=0401','12&sub=1201','9&sub=0901','6&sub=0601','8&sub=0801','5&sub=0501','10&sub=1001','7&sub=0701','11&sub=1101','3&sub=0301','13&sub=1301','1&sub=0101','2&sub=0201']
	# url = 'http://www.punoftheday.com/cgi-bin/disppuns.pl?ord=S&cat=4&sub=0401&page='

	i = 0
	punindex = 0
	puns = {"My girlfriend criticised my apartment, so I knocked her flat"}
	print "My girlfriend criticised my apartment, so I knocked her flat"

	# for every category in the valid categories
	for cat in validcats:
		# form the initial link
		url = urlhalf + cat + urlotherhalf
		# loop through 10 pages of the category
		for i in xrange(1,11):
			# parsing the page to get only table containing puns
			# print url + str(i)
			page = requests.get(url + str(i))
			tree = html.fromstring(page.text)
			htmlpage = html.tostring(tree)
			htmlpage = htmlpage.split("<!-- Puns -->")[1]
			htmlpage = htmlpage.split("<!-- google_ad_section")[0]
				
			# for each line in that table
			for line in htmlpage.split("\n"):
				# process only the ones that have the pun
				if '<div class="credit"' in line:
					linepun = line[line.index("<td>") + len("<td>"):line.index("<div class=")]
					if linepun not in puns:
						print linepun
						puns.add(linepun)