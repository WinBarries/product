"""
Name: Kabir Bolatito
"""
import urllib
import urllib.request
from bs4 import BeautifulSoup

url = "https://twitter.com/iamtito_"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

print(soup.title.text)
#print(soup.findAll('a'))
"""
for eachLink in soup.findAll('a'):
	print(eachLink.get('href'))
	print(eachLink.text)
"""
print(soup.find('div',{"class":"ProfileHeaderCard"}).find('p').text)
print ("----------")

i = 1
for tweets in soup.findAll('div', {"class":"content"}):
	print(i)
	print(tweets.find('p').text)
	#print(tweets.text)
	i = i+1
