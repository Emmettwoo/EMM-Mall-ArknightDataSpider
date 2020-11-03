# coding=utf-8
import urllib2

from pip._vendor import requests


# 网页下载模块
class Downloader:
    def __init__(self):
        pass

    @staticmethod
    def download(url):
        if url is None:
            return None

        # print ("Downloading: " + url)
        response = urllib2.urlopen(url, timeout=5)

        if response.getcode() != 200:
            return None
        return response.read()

    @staticmethod
    def save_image(img_url, img_name):
        if img_url != "http:":
            # print ("Downloading: " + img_name)
            content = requests.get(img_url).content
            with open(img_name, 'wb') as f:
                f.write(content)
