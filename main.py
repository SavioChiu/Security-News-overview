import requests,re,json
from bs4 import BeautifulSoup

def securityweek()->list:

    securityweek_news = []

    response = requests.get('https://www.securityweek.com')
    soup = BeautifulSoup(response.content,"html.parser")

    div_tag = soup.find_all("div",class_="view view-lastest-security view-id-lastest_security view-display-id-block_1 view-dom-id-3")
    span_tag = div_tag[0].find_all("span",class_="field-content")

    for tag in span_tag:
        securityweek_news.append( {'Type':'security week','Title':tag.string,'Link':f'https://www.securityweek.com{tag.find_all("a")[0].get("href")}'})
    return securityweek_news

def bleepingcomputer()->list:

    bleepingcomputer_news = []

    response = requests.get('https://www.bleepingcomputer.com')
    soup = BeautifulSoup(response.content, "html.parser")
    div_tag = soup.find_all("div",class_="bc_latest_news")
    li_tag = div_tag[0].find_all("li")
    for tag in li_tag:
        if tag.find_all("div",class_="bc_latest_news_category")[0].find_all("a")[0].string == 'SECURITY':
            bleepingcomputer_news.append( {'Type':'bleeping computer','Title':tag.find_all("a")[0].string,'Link':tag.find_all("a")[0].get('href')} )

    print(bleepingcomputer_news)

def thehackernews()->list:

    thehackernews_news = []

    response = requests.get('https://thehackernews.com')

bleepingcomputer()