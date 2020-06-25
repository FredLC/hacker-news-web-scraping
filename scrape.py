import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtexts = soup.select('.subtext')

def sort_stories_by_votes(newslist):
	return sorted(newslist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtexts):
	hn = []
	for index, item in enumerate(links):
		title = item.getText()
		hrefs = item.get('href', None)
		vote = subtexts[index].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title': title, 'link': hrefs, 'votes': points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtexts))