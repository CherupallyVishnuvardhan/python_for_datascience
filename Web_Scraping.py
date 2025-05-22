from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re
#Scraping a Webpage and Saving your results
r=urllib.request.urlopen('https://analytics.usa.gov').read()
soup=BeautifulSoup(r,'html.parser')
print(type(soup))

print(soup.prettify()[0:100])

for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.get_text())

print(soup.find_all()[0:1000])

for link in soup.find_all('a',attrs= {'href': re.compile('^http')}):
    print(link)
    
print(type(link))

file=open('parsed_data.txt','w')

for link in soup.find_all('a', attrs= {'href': re.compile('^http')}):
    soup_link= str(link)
    print(soup_link)
    file.write(soup_link)
file.flush()
file.close()
pwd