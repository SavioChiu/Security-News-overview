import requests, webbrowser
import tkinter
from tkinter import font
from bs4 import BeautifulSoup

class web_clawer:

    def __init__(self):

        self.news = []

        self.reload()
        self.gui()

        # for i in range(len(self.news)):
        #     print(f"{self.news[i]['Title']} | {self.news[i]['Type']} | {self.news[i]['Time']}",end='\n<-------------------------------->\n')

    def security_week(self):

        response = requests.get('https://www.securityweek.com')
        soup = BeautifulSoup(response.content,"html.parser")

        div_tag = soup.find_all("div",class_="view view-lastest-security view-id-lastest_security view-display-id-block_1 view-dom-id-3")
        span_tag = div_tag[0].find_all("span",class_="field-content")

        for tag in span_tag:
            self.news.append(
                    {
                    'Type':'security week',
                    'Title':tag.string,
                        'Link':f'https://www.securityweek.com{tag.find_all("a")[0].get("href")}',
                    'Time': ''
                    }
            )

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
                         'Link': tag.find_all("a")[0].get('href'),
                         'Time': ''
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
                 'Link': tag.find_all("a",class_="story-link")[0].get('href'),
                 'Time':''
                 }
            )

    def reload(self):
        self.security_week()
        self.bleeping_computer()
        self.hacker_news()

    def listbox_select(self,event):

        selected = self.listbox.get(self.listbox.curselection()[0])

        for i in range(0,len(self.news)):
            if self.news[i]["Title"] in selected:
                webbrowser.open(self.news[i]["Link"])
                break
            else: pass

    def gui(self):

        counter = 1

        root = tkinter.Tk()
        root.title('web_crawler')
        root.geometry('1000x440')

        listbox_format = '{title:^100}|{source:^20}|{time:^20}'
        font1 = font.Font(family='consolas', size='10')

        scrollbar = tkinter.Scrollbar(root)
        self.listbox = tkinter.Listbox(root, width=200, height=25, font=font1, yscrollcommand=scrollbar.set)
        self.listbox.bind('<ButtonRelease-1>',self.listbox_select)
        self.listbox.bind('<Return>',self.listbox_select)
        scrollbar.config(command=self.listbox.yview)

        self.listbox.insert(0, listbox_format.format(title='Title', source='Source', time='Time'))
        for item in self.news:
            self.listbox.insert(counter,listbox_format.format(title=item['Title'],source=item['Type'],time=item['Time']))
            counter += 1

        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.listbox.pack()

        reload = tkinter.Button(root,text='Reload',command=self.reload)
        #reload.bind('<Return>',lambda event: print('pressed F5 key'))
        reload.pack()

        root.mainloop()

obj = web_clawer()
