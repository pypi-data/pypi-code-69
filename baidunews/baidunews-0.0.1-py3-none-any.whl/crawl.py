# -*- coding:utf-8 -*-

# __author:ly_peppa
# date:2020/11/23


# 0.0.1更新：googlenews改为baidunews



import re
import requests
from bs4 import BeautifulSoup
from BaiduNews import info
import time
import random
import datetime
from urllib import parse
import pandas as pd


class BaiduNews():

    def __init__(self):
        self.author_wx = 'ly_peppa'
        self.author_qq = '3079886558'
        self.author_email = 'iseu1130@sina.cn'
        self.urls = {}                      # 目标网页
        self.headers = {}                   # Get/Post请求头
        self.param = {}
        self.cookie=requests.cookies.RequestsCookieJar()
        self.session = requests.session()
        self.keywords=None
        self.df_search=None
        self.df_detail=None

    # 从配置文件中更新登录链接信息
    def update_info(self):
        self.urls = info.loginUrls                                                  #http地址
        self.headers = info.loginHeaders
        self.param = info.loginParam
        self.cookie.set("cookie", info.loginCookie)
        self.session.cookies.update(self.cookie)

    # 发送Get请求
    def requests_get(self, url, data=None, headers=None):
        try:
            url = url if data is None else url+parse.urlencode(data)
            time.sleep(random.random() * 0.5 + 0.1)  # 0-1区间随机数
            #没有缓存就开始抓取
            print(self.urls['proxies']['https'] + ' --> ' + url)
            # response = self.session.get(url, proxies=self.proxy, headers=headers, verify=False)
            # self.session.keep_alive = False
            response = requests.get(url, headers=headers, timeout=10)
            response.encoding = response.apparent_encoding
            value = response if response.status_code == requests.codes.ok else None
        except Exception as e:
            value = None
        finally:
            return value

    # 搜索新闻
    def search_news(self, keywords, day=-365*50, pn=None):
        self.keywords = keywords
        result=None
        try:
            self.df_search = pd.DataFrame(columns=["Keywords", "Title", "Url", "Summary", "Source", "Stamp"])
            self.param['news']['word']=self.keywords
            self.param['news']['pn'] = -10

            self.news_next(keywords, day=day, pn=pn)

            result=self.df_search

        except Exception as e:
            print(e)
        finally:
            return result

    # 搜索新闻
    def news_next(self, keywords, day=-365*50, pn=None):
        result=None
        try:
            if pn is not None:
                if self.param['news']['pn']>pn:
                    return result
            self.param['news']['pn'] = self.param['news']['pn'] + 10
            response = self.requests_get(self.urls['news'], self.param['news'], headers=self.headers['news'])
            if response is None:
                return result
            soup = BeautifulSoup(response.text, "html.parser")
            content_left = soup.find('div', id='content_left')
            page_inner = soup.find('div', id='page').find('a', text='下一页 >')
            news_normal=content_left.find_all('div',attrs={'class':re.compile("result-op c-container xpath-log new-pmd"), 'srcid': '1599', 'tpl': 'news-normal'})
            for new_normal in news_normal:
                news_title=new_normal.a.text.strip()
                news_url=new_normal.a['href']
                spans = new_normal.find('div', class_='news-source').find_all('span')
                news_source=spans[0].text.strip()
                news_stamp=spans[1].text.strip()
                span = new_normal.find('span', class_='c-font-normal c-color-text')
                news_summary=span.text.strip()
                try:
                    news_date = datetime.datetime.strptime(news_stamp, "%Y年%m月%d日 %H:%M")
                    now = datetime.datetime.now()
                    delta = datetime.timedelta(days=day)
                    pre_date = now + delta
                    if news_date < pre_date:
                        continue
                except:
                    news_stamp = ""

                row=[keywords, news_title, news_url, news_summary, news_source, news_stamp]
                # print(row)
                self.df_search.loc[len(self.df_search)]=row
            if page_inner:
                self.news_next(keywords, day=day, pn=pn)
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
        self.update_info()
        df_search=self.search_news('中国银行 电子银行',day=-3, pn=None)
        print(df_search)

        df_detail=self.news_detail(top=10)
        print(df_detail)

        self.news_save()


if __name__ == '__main__':

    ac=BaiduNews()
    ac.start()


