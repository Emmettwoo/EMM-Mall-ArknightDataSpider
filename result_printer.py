# coding=utf-8
import os
import spider_config

from time import strftime, gmtime


# 结果输出模块
class ResultPrinter(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('result.html', 'w')
        fout.write("<html>")
        fout.write("<head>")
        fout.write('<meta charset="utf-8" />')
        fout.write("<title>Crawl Result</title>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write('<h1 style="text-align:center">Crawl Result</h1>')
        fout.write('<table style="border-collapse:collapse;"  border="1">')
        fout.write("<tr>")
        fout.write("<td>中文名称</td>")
        fout.write("<td>英文名称</td>")
        fout.write("<td>干员类型</td>")
        fout.write("<td>干员星级</td>")
        fout.write("<td>干员图片</td>")
        fout.write("</tr>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td><a href='%s'>%s</a></td>" % (data["url"].encode("utf-8"), data["name_cn"].encode("utf-8")))
            fout.write("<td>%s</td>" % data["name_en"])
            fout.write("<td>%s</td>" % data["class"])
            fout.write("<td>%s</td>" % data["stars"])
            # 图片循环
            os.chdir(data['name_en'])
            count = 1
            while 1:
                if os.path.exists(data['name_en'] + "_img-" + str(count) + ".png"):
                    fout.write("<td><img src='%s/%s_img-%s.png' width=80px></td>"
                               % (data['name_en'], data['name_en'], str(count)))
                    count = count + 1
                else:
                    break
            fout.write("</tr>")
            os.chdir("../")

        fout.write("</table>")
        fout.write('<br /><br /><p style="text-align:center">Power By Emmett Woo</p>')
        fout.write("</body>")
        fout.write("</html>")

    def output_sql(self):
        if spider_config.CoverMode:
            fout = open('result.sql', 'w')
            fout.write("truncate table mall_product;\n")
            count = 1
        else:
            fout = open('result.sql', 'a')
            count = len(spider_config.workingDir) + 1

        for data in self.datas:
            time_now = strftime("%Y-%m-%d %H:%M:%S", gmtime()).decode('utf-8')
            sql_head = "INSERT INTO `mall_product` (`id`, `category_id`, `name`, `subtitle`, `main_image`, " \
                       "`sub_images`, `detail`, `price`, `stock`, `status`, `create_time`, `update_time`) VALUES "
            sql_body = '''(%s, %s, '%s', '%s', '%s/%s_img-1.png', '%s', '%s', %s, 1024, 1, '%s', '%s')''' % \
                       (str(count), data['class'], data['name_cn'], data['name_en'], data['name_en'], data['name_en'],
                        self.get_image_urls(data['name_en']), self.get_describe(data['name_en']), data['stars'],
                        time_now, time_now)
            fout.write(sql_head + sql_body + ";\n")
            count = count + 1

    @staticmethod
    def get_image_urls(name_en):
        image_urls = ""
        os.chdir(name_en)
        count = 1
        while 1:
            if os.path.exists(name_en + "_img-" + str(count) + ".png"):
                image_urls = image_urls + ("%s/%s_img-%s.png," % (name_en, name_en, str(count)))
                count = count + 1
            else:
                break
        os.chdir("../")
        return image_urls[0:-1]

    @staticmethod
    def get_describe(name_en):
        describe = ""
        os.chdir(name_en)
        count = 1
        while 1:
            if os.path.exists(name_en + "_img-" + str(count) + ".png"):
                describe = describe + ('<img src="http://q.woohoo.top/%s/%s_img-%s.png" width="512px">\n'
                                       % (name_en, name_en, str(count)))
                count = count + 1
            else:
                break
        os.chdir("../")
        return describe
