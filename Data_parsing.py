from bs4 import BeautifulSoup

import urllib
import urllib.request
import re

with urllib.request.urlopen('https://raw.githubusercontent.com/BigDataGal/Data-Mania-Demos/master/IoT-2018.html') as response:
    html=response.read()

soup= BeautifulSoup(html,'html.parser')
print(type(soup))

print(soup.prettify()[0:100])

#Getting data from parse tree
text_only=soup.get_text()
print(text_only)

print(soup.find_all('li'))

#Retrieving tags by filtering with keyword arguments

print(soup.find_all(id='link 7'))

#Retrieving tags by filtering with string arguments

print(soup.find_all('ol'))

#Retrieving tags by filtering with list objects

print(soup.find_all(['li','b']))

#Retrieving tags by filtering with regular expressions

t=re.compile('t')
for tag in soup.find_all(t):
    print(tag.name)
    
    
#Retrieving tags by filtering with a Boolean value
for tag in soup.find_all(True):
    print(tag.name)
    
print(soup.find_all(t))

#Retrieving weblinks by filtering with string objects

for link in soup.find_all('a'):
    print(link.get('href'))
    
#Retrieving strings by filtering with regular expressions
print(soup.find_all(string=re.compile('data')))