# coding=utf-8
import os

# 覆盖模式，默认关闭，开启后会覆盖爬取已存在档案
# workingDir列举当前工作目录下的子目录，用于判断档案是否已存在
CoverMode = 0
workingDir = os.listdir("./")

# 干员类型<图片链接>对应的<数据库编号>
char_class_links = {
    # 先锋干员
    "http://prts.wiki/images/8/82/%E5%9B%BE%E6%A0%87_%E8%81%8C%E4%B8%9A_%E5%85%88%E9%94%8B_%E5%A4%A7%E5%9B%BE.png": "1",
    # 近卫干员
    "http://prts.wiki/images/a/a9/%E5%9B%BE%E6%A0%87_%E8%81%8C%E4%B8%9A_%E8%BF%91%E5%8D%AB_%E5%A4%A7%E5%9B%BE.png": "2",
    # 狙击干员
    "http://prts.wiki/images/d/d1/%E5%9B%BE%E6%A0%87_%E8%81%8C%E4%B8%9A_%E7%8B%99%E5%87%BB_%E5%A4%A7%E5%9B%BE.png": "3",
    # 重装干员
    "http://prts.wiki/images/6/6f/%E5%9B%BE%E6%A0%87_%E8%81%8C%E4%B8%9A_%E9%87%8D%E8%A3%85_%E5%A4%A7%E5%9B%BE.png": "4",
    # 医疗干员
    "http://prts.wiki/images/b/b8/%E5%9B%BE%E6%A0%87_%E8%81%8C%E4%B8%9A_%E5%8C%BB%E7%96%97_%E5%A4%A7%E5%9B%BE.png": "5",
    # 辅助干员
    "http://prts.wiki/images/f/f0/%E5%9B%BE%E6%A0%87_%E8%81%8C%E4%B8%9A_%E8%BE%85%E5%8A%A9_%E5%A4%A7%E5%9B%BE.png": "6",
    # 术士干员
    "http://prts.wiki/images/4/4d/%E5%9B%BE%E6%A0%87_%E8%81%8C%E4%B8%9A_%E6%9C%AF%E5%B8%88_%E5%A4%A7%E5%9B%BE.png": "7",
    # 特种干员
    "http://prts.wiki/images/2/2a/%E5%9B%BE%E6%A0%87_%E8%81%8C%E4%B8%9A_%E7%89%B9%E7%A7%8D_%E5%A4%A7%E5%9B%BE.png": "8"
}

# 干员类型<星级链接>对应的<数据库编号>
char_stars_links = {
    "http://prts.wiki/images/0/06/%E7%A8%80%E6%9C%89%E5%BA%A6_%E7%99%BD_0.png": "1",
    "http://prts.wiki/images/8/8a/%E7%A8%80%E6%9C%89%E5%BA%A6_%E7%99%BD_1.png": "2",
    "http://prts.wiki/images/6/66/%E7%A8%80%E6%9C%89%E5%BA%A6_%E7%99%BD_2.png": "3",
    "http://prts.wiki/images/4/49/%E7%A8%80%E6%9C%89%E5%BA%A6_%E7%99%BD_3.png": "4",
    "http://prts.wiki/images/b/bf/%E7%A8%80%E6%9C%89%E5%BA%A6_%E7%99%BD_4.png": "5",
    "http://prts.wiki/images/c/cf/%E7%A8%80%E6%9C%89%E5%BA%A6_%E7%99%BD_5.png": "6"
}
