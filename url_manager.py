# coding=utf-8
import re


# URL管理模块
class UrlManager:
    def __init__(self):
        self.url_set = set()

    def init_root_url(self, root_url, soup):
        # 获取 注释与链接 中的 干员一览 部分
        links = soup.find('table', class_="nowraplinks collapsible uncollapsed navbox-inner")
        # 循环 干员一览 内的所有超链接
        for link in links.find_all('a', href=re.compile(r"/w/")):
            # 如果目标地址不(包含)以 "分类:" 开头，则为干员链接
            if "%E5%88%86%E7%B1%BB:" not in link.get('href'):
                self.url_set.add("http://prts.wiki/" + link.get('href'))
        # 最后，根路径也是目标干员信息之一
        self.url_set.add(root_url)

    def has_new_url(self):
        return len(self.url_set) != 0

    def get_new_url(self):
        return self.url_set.pop()