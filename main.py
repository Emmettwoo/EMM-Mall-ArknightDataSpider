# coding=utf-8
import os
import spider_config

from bs4 import BeautifulSoup
from url_manager import UrlManager
from downloader import Downloader
from content_parser import ContentParser
from result_printer import ResultPrinter


# 主程序入口
class SpiderMain:
    def __init__(self):
        pass


def change_working_dir():
    if 'data' not in os.listdir("./"):
        os.mkdir('data')
    os.chdir('data')
    spider_config.workingDir = os.listdir("./")


def craw(root_url):
    soup = BeautifulSoup(downloader.download(root_url), 'html.parser', from_encoding='utf-8')
    urlManager.init_root_url(root_url, soup)

    # 根据url列表爬取网页
    while urlManager.has_new_url():
        try:
            new_url = urlManager.get_new_url()
            html_cont = downloader.download(new_url)
            new_data = parser.parse(new_url, html_cont)
            printer.collect_data(new_data)
        except:
            print "crawl failed!"
    printer.output_sql()


# 程序执行
if __name__ == "__main__":
    print "Welcome to EMM-Mall-ArknightDataSpider."

    # 各模块初始化(实例化)
    urlManager = UrlManager()
    downloader = Downloader()
    parser = ContentParser()
    printer = ResultPrinter()

    # 实例化主入口，开始爬取数据
    SpiderMain = SpiderMain()
    change_working_dir()
    # craw(raw_input("Enter Root Url : "))
    craw("http://prts.wiki/w/Lancet-2")

    print ("Everything is done. Result is in result.sql")
