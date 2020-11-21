# -*- coding:utf-8 -*-

# __author:ly_peppa
# date:2020/11/18


# 0.0.6更新：增加中文搜索的支持，解决news_detail的乱码导出失败问题



import re
import requests
from bs4 import BeautifulSoup
import time
import random
import datetime
import pandas as pd


class GoogleNews():

    def __init__(self):
        self.author_wx = 'ly_peppa'
        self.author_qq = '3079886558'
        self.author_email = 'iseu1130@sina.cn'
        self.url = 'https://news.google.com'
        self.base = {'US': 'https://news.google.com/search?q={:s}&hl=en-US&gl=US&ceid=US%3Aen',
                     'CN': 'https://news.google.com/search?q={:s}&hl=zh-CN&gl=CN&ceid=CN%3Azh-Hans',
                     }
        # self.base = 'https://news.google.com/search?q={:s}&hl=en-US&gl=US&ceid=US%3Aen' if gl=='US' else 'https://news.google.com/search?q={:s}&hl=zh-CN&gl=CN&ceid=CN%3Azh-Hans'
        # self.base = 'https://news.google.com/search?q={:s}&hl=en-US&gl=US&ceid=US%3Aen'
        # self.base = 'https://news.google.com/search?q={:s}&hl=zh-CN&gl=CN&ceid=CN%3Azh-Hans'
        self.proxy={'http':'127.0.0.1:80'}
        self.keywords=None
        self.df_search=None
        self.df_detail=None


    # 发送Get请求
    def requests_get(self, url):
        response = None
        try:
            print(url)
            # time.sleep(random.random() * 0.5 + 0.1)  # 暂停随机数
            response=requests.get(url, proxies=self.proxy, timeout=10)
            # response.encoding='utf-8'
            response.encoding = response.apparent_encoding
        except Exception as e:
            print(e)
        finally:
            return response

    # 搜索新闻
    def search_news(self, keywords, day=-365*50, gl='US'):
        self.keywords=keywords
        search_url = self.base[gl].format(keywords.replace(' ','%20'))
        result=None
        try:
            self.df_search = pd.DataFrame(columns=["Keywords", "Title", "Url", "Summary", "Source", "Stamp"])
            response = self.requests_get(search_url)
            if response is None:
                return result
            # print(response)
            soup = BeautifulSoup(response.text, "html.parser")
            NiLAwe = soup.find_all('div', class_='NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc', jslog='93789')
            # print(NiLAwe.__len__())
            for item in NiLAwe:
                ipQwMb = item.find('h3', class_='ipQwMb ekueJc RD0gLb')
                news_title=ipQwMb.a.text.strip()
                news_url = self.url+ipQwMb.a['href'][1:]
                jVqMGc = item.find('div', class_='Da10Tb Rai5ob', jsname='jVqMGc')
                news_summary=jVqMGc.span.text.strip()
                SVJrMe = item.find('div', class_='SVJrMe', jsname='Hn1wIf')
                news_source=SVJrMe.a.text.strip()
                try:
                    news_stamp = SVJrMe.time['datetime']
                    news_date = datetime.datetime.strptime(news_stamp, "%Y-%m-%dT%H:%M:%SZ")
                    now = datetime.datetime.now()
                    delta = datetime.timedelta(days=day)
                    pre_date = now + delta
                    if news_date < pre_date:
                        continue
                except:
                    news_stamp = ""

                row=[keywords, news_title, news_url, news_summary, news_source, news_stamp]
                self.df_search.loc[len(self.df_search)]=row
                # print(row)
            result=self.df_search

        except Exception as e:
            print(e)
        finally:
            return result

    # 查看详情
    def news_detail(self, top=100):
        result=None
        try:
            if self.df_search is None:
                print('self.df_search is None, self.search_news() first')
                return
            self.df_detail = pd.DataFrame(columns=["Keywords", "Title", "Url", "Summary", "Source", "Stamp", "Text", "Content"])
            for index, row in self.df_search.iterrows():
                if index>=top:
                    continue
                try:
                    response = self.requests_get(row['Url'])
                    if response is None:
                        row['Text'] = "error"
                        row['Content']="error"
                    else:
                        row['Text'] = self.html_text(response.text)
                        row['Content']=self.extract_article(response.text)
                    # row['CleanedData'] = self.datacleaning(row['Content'], self.keywords)
                    # row['Sentiment'] = self.textblob_sentiment(row['CleanedData'])
                    # soup = BeautifulSoup(response.text, "html.parser")
                    # gettext = soup.get_text().strip()
                    # row['html'] = response
                    # row['text'] = gettext

                    self.df_detail.loc[len(self.df_detail)] = row
                except Exception as e:
                    print(e)
                    continue

            result = self.df_detail
            # result = self.df_detail.applymap(lambda x: x.encode('unicode_escape').
            #                            decode('utf-8') if isinstance(x, str) else x)

        except Exception as e:
            print(e)
        finally:
            return result

    # 保存
    def news_save(self):
        if self.df_detail is not None:
            self.df_detail.to_csv('detail_{:s}.csv'.format(self.keywords), encoding='utf_8_sig')
            self.df_detail.to_excel('detail_{:s}.xlsx'.format(self.keywords))
            return
        if self.df_search is not None:
            self.df_search.to_csv('search_{:s}.csv'.format(self.keywords), encoding='utf_8_sig')
            self.df_search.to_excel('search_{:s}.xlsx'.format(self.keywords))


    # 获取网页文本
    def html_text(self, web_content):
        result=None
        try:
            soup = BeautifulSoup(web_content, "html.parser")
            result=soup.get_text().strip()
        except Exception as e:
            print(e)
        finally:
            return result

    def extract_article(self, web_content):
        # 防止遇到error卡退
        result="error"
        try:
            soup = BeautifulSoup(web_content, 'lxml')
            articleContent = soup.find_all('p')
            article = []
            for p in articleContent:
                article.append(p.text)
            result = '\n'.join(article).strip()
        except Exception as e:
            print(e)
        finally:
            return result


    def datacleaning(self, text, keyword):
        pattern = re.compile("[,;.，；。]+[^,;.，；。]*" + keyword + "+[^,;.，；。]*[,;.，；。]+")
        result = re.findall(pattern, text)
        for i in range(len(result)):
            result[i] = result[i].replace("\xa0", " ")
            result[i] = result[i].replace("\n", "")
        str = '>>'.join(result)
        return str

    # def textblob_sentiment(self, text):
    #     blob = TextBlob(text)
    #     return blob.sentiment


    def print_df(self, df):
        for index, row in df.iterrows():
            print(index)
            print(row)


    def start(self):

        df_search=self.search_news('Didi financial crisis')
        print(df_search)

        df_detail=self.news_detail(10)
        print(df_detail)

        self.news_save()


if __name__ == '__main__':

    ac=GoogleNews()
    ac.start()


