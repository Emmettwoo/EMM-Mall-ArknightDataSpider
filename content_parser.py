# coding=utf-8
import os
import spider_config

from bs4 import BeautifulSoup
from downloader import Downloader
downloader = Downloader()


# 网页解析模块
class ContentParser:

    def __init__(self):
        global downloader

    @staticmethod
    def get_page_data(page_url, soup):
        page_data = {'url': page_url}

        # 干员英文名称: <div class="charname-en anicss" id="charname-en">Lancet-2</div>
        name_en_node = soup.find('div', class_="charname-en anicss")
        # 去除名称中的空格和单引号，以免引起奇奇怪怪的bug
        page_data['name_en'] = name_en_node.get_text().replace(" ", "").replace("'", "")
        # print("page_data['name_en']: ", page_data['name_en'])

        # 如果角色已存在，决定覆盖或者跳过
        if page_data['name_en'] in spider_config.workingDir and spider_config.CoverMode != 1:
            print("Character Exist.")
            return

        # 干员中文名称：<div class="charname anicss" id="charname">Lancet-2</div>
        name_cn_node = soup.find('div', class_="charname anicss")
        page_data['name_cn'] = name_cn_node.get_text()
        # print("page_data['name_cn']: ", page_data['name_cn'])

        # 干员类型
        class_node = soup.find('div', class_="charclass anicss").find("img")
        page_data['class'] = spider_config.char_class_links[class_node.get("src")]
        # print("page_data['class']: ", page_data['class'])

        # 干员星级
        stars_node = soup.find('div', class_="starimg").find("img")
        page_data['stars'] = spider_config.char_stars_links[stars_node.get("src")]
        # print("page_data['stars']: ", page_data['stars'])

        # 干员图片
        if page_data['name_en'] not in spider_config.workingDir:
            os.mkdir(page_data['name_en'])
        os.chdir(page_data['name_en'])
        # 如果是第一张图，则跳过（初始图 和 阶段一 图是重复的）
        count = 0
        # 遍历角色原始图片（精英阶段一 和 精英阶段二）
        for img_node in soup.find_all('div', class_="charimg-stage"):
            if count != 0:
                try:
                    downloader.save_image(img_node.find("img").get("src"),
                                          page_data['name_en'] + "_img-" + str(count) + ".png")
                except:
                    continue
            count = count + 1

        # 遍历角色皮肤图片
        for img_node in soup.find_all('div', class_="charimg-skin"):
            try:
                downloader.save_image(img_node.find("img").get("src"),
                                      page_data['name_en'] + "_img-" + str(count) + ".png")
            except:
                continue
            count = count + 1

        os.chdir("../")

        return page_data

    def parse(self, page_url, html_cont):
        if page_url is None:
            return
        else:
            print ("Parsing: " + page_url)
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
            new_data = self.get_page_data(page_url, soup)
            return new_data
