from lxml import html
import re
import requests


def _get_origin(tree):
	'''
		Return a dictionary with the year in which the word was first used and
		a broader description of its origins.
	'''
	# Some words use XPATH1 to segway into the origins section, but some use
	# XPATH2 instead. We will need to account for both.
	XPATH1 = '//div[@class="etymology"]/div//text()'
	XPATH2 = '//div[@class="first-use"]/div/text()'
	DATE_PREFIX = 'First Known Use:' # prefixes date/year in XPATH1
	
	initial = tree.xpath(XPATH1)
	alternate = tree.xpath(XPATH2)
	# Usual processing
	origin = [_trim(elem) for elem in initial + alternate if _trim(elem)]
	origin_results = {'origin_date': set(), 'origin_description': set()}

	for detail in origin:
		# Date if prefixed by 'First Known Use:' (XPATH1) or if value is
		# in XPATH2's results
		if DATE_PREFIX in detail or detail in alternate:
			origin_results['origin_date'].add(detail.strip(DATE_PREFIX))
		# If not date, then origin textual description
		else:
			origin_results['origin_description'].add(detail)

	return origin_results






if __name__ == '__main__':

	word = '1'
	url = ''.join(['http://www.punoftheday.com/cgi-bin/disppuns.pl?ord=S&cat=4&sub=0401&page=', word])
	page = requests.get(url)
	tree = html.fromstring(page.text)

	htmlpage = html.tostring(tree)
	htmlpage = htmlpage.split("<!-- Puns -->")[1]
	htmlpage = htmlpage.split("<!-- google_ad_section")[0]

	# Parse, and assemble results in dict.

	print htmlpage