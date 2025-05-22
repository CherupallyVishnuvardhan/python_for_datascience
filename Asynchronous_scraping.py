import aiohttp
import asyncio

from bs4 import BeautifulSoup
import csv
import re

import nest_asyncio
nest_asyncio.apply()

async def scrap_and_save_links(text):
    soup=BeautifulSoup(text,'html.parser')
    file=open('csv_file','a',newline='')
    writer=csv.writer(file,delimiter=',')
    for link in soup.findAll('a',attrs={'href':re.compile('^http')}):
        link=link.get('href')
        writer.writerow([link])
    file.close()
async def fetch(session,url):
    try:
        async with session.get(url) as response:
            text=await response.text()
            task=asyncio.create_task(scrap_and_save_links(text))
            await task
    except Exception as e:
        print(str(e)) 

async def scrap(urls):
    tasks=[]
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session,url)) 
        await asyncio.gather(*tasks)
urls=['https://analytics.usa.gov','https://www.python.org','https://www.linkedin.com/']
asyncio.run(scrap(urls=urls))      