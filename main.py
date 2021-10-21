import requests
from bs4 import BeautifulSoup

class web_clawer:

    def __init__(self):

        self.news = []

        self.security_week()
        self.bleeping_computer()
        self.hacker_news()

        for i in self.news:
            print(i)

    def security_week(self):

        response = requests.get('https://www.securityweek.com')
        soup = BeautifulSoup(response.content,"html.parser")

        div_tag = soup.find_all("div",class_="view view-lastest-security view-id-lastest_security view-display-id-block_1 view-dom-id-3")
        span_tag = div_tag[0].find_all("span",class_="field-content")

        for tag in span_tag:
            self.news.append( {'Type':'security week','Title':tag.string,'Link':f'https://www.securityweek.com{tag.find_all("a")[0].get("href")}'})

    def bleeping_computer(self):

        response = requests.get('https://www.bleepingcomputer.com')
        soup = BeautifulSoup(response.content, "html.parser")
        id_tag = soup.find_all("ul",id="bc-home-news-main-wrap")
        li_tag = id_tag[0].find_all("li", class_=None, recursive=False)

        for tag in li_tag:
            for i in tag.find_all("div", class_="bc_latest_news_category")[0].find_all("a"):
                if i.string == 'Security':

                    self.news.append(
                        {'Type': 'bleeping computer',
                         'Title': tag.find_all("h4")[0].string,
                         'Link': tag.find_all("a")[0].get('href')
                         }
                    )

                else: pass

    def hacker_news(self):

        response = requests.get('https://thehackernews.com/')
        soup = BeautifulSoup(response.content, "html.parser")
        div_tag = soup.find_all("div",class_="body-post clear")
        for tag in div_tag:
            self.news.append(
                {'Type': 'hacker news',
                 'Title': tag.find_all("h2")[0].string,
                 'Link': tag.find_all("a",class_="story-link")[0].get('href')
                 }
            )

obj = web_clawer()
