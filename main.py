import requests,re
from bs4 import BeautifulSoup
urls = [
    'https://www.securityweek.com',
    'https://www.bleepingcomputer.com',
    'https://www.helpnetsecurity.com/view/news',
    'https://thehackernews.com'
]
securityweek_news = []

request = requests.get('https://www.securityweek.com')
out = request.content
soup = BeautifulSoup(out,'html.parser')
strhtm = soup.prettify()
with open('test.html','w') as f:
    f.write(strhtm)
    f.close()
with open('test.html','r') as f:
    reader = f.readlines()
    for line in range(len(reader)):
        if re.search('<span class="field-content">',reader[line]):
            securityweek_news.append( reader[line+1].replace('<a href="','').replace('">','').replace(' ','').replace('\n',''))
        else: pass
    f.close()
    print(securityweek_news)

# print(out)