# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class WeatherPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        with open('weather.txt', 'w+') as file:
            city = item['city']
            file.write('city:' + city + '\n\n')
            date = item['date']
            desc = item['dayDesc']
            print("============="+str(desc)+"=============")
            dayDesc = desc[1::2]
            nightDesc = desc[0::2]

            dayTemp = item['dayTemp']

            weaitem = list(zip(date, dayDesc, nightDesc, dayTemp))

            for i in range(len(weaitem)):
                item = weaitem[i]
                d = item[0]
                dd = item[1]
                nd = item[2]
                ta = item[3].split('/')
                dt = ta[0]
                nt = ta[1]
                txt = 'date:{0}\t\tday:{1}({2})\t\tnight:{3}({4})\n\n'.format(
                    d,
                    dd,
                    dt,
                    nd,
                    nt
                )
                file.write(txt)
        return item
