# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
from .items import MainItem
from scrapy.exceptions import DropItem
from similarity.normalized_levenshtein import NormalizedLevenshtein
from similarity.jarowinkler import JaroWinkler
from similarity.jaccard import Jaccard
import datetime

class MappingPipeline(object):

    def process_item(self, item, spider):

        if item['source'] == 'travel':
            new_item = MainItem(
                source = item['source'],
                name_tour = item['title'],
                type_tour =item['type_tour'],
                url_tour = item['url_tour'],
                cost_tour = item['cost_tour'],
                number_date = item['number_date'],
                start_date = item['start_date']
            )
            return new_item
        if item['source'] == 'khviet':
            new_item = MainItem(
                source = item['source'],
                name_tour = item['title'],
                type_tour =item['type_tour'],
                url_tour = item['url_tour'],
                cost_tour = item['cost_tour'],
                number_date = item['number_date'],
                start_date = item['begin_date']
            )
            return new_item
        if item['source'] == 'vietT':
            new_item = MainItem(
                source = item['source'],
                name_tour = item['name_tour'],
                type_tour =item['type_tour'],
                url_tour = item['link'],
                cost_tour = item['cost_tour'],
                number_date = item['number_date'],
                start_date = item['start_date']
            )
            return new_item


class NormalizeNumberDatePipeline(object):


    @staticmethod
    def parse_number(number, cost, url):

        urlNew = url.replace('-', ' ').replace('/', ' ')
        if urlNew.find("ngay") != -1:
            for s in urlNew.split():
                if s.isdigit():
                    return s

        if number is None:
            return number
        else:
            numberNew = number.replace('/', ' ')
            tmp = numberNew.find('VNĐ')
            if tmp == -1:   
                for s in number.split():
                    if s.isdigit():
                        return s
            else:
                if cost is None:
                    return cost
                else:
                    tmp = cost.replace('.', '').replace(',', '')
                    for s in tmp.split():
                        if s.isdigit():
                            return s
     
        return None

    def process_item(self, item, spider):
        item['number_date'] = self.parse_number(item['number_date'], item['cost_tour'], item['url_tour'])
        return item

class NormalizeTypePipeline(object):
    global check
    global check_address

    # INTAB = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ"
    # INTAB = [ch.encode('utf8') for ch in unicode(INTAB, 'utf8')]

    # OUTTAB = "a"*17 + "o"*17 + "e"*11 + "u"*11 + "i"*5 + "y"*5 + "d"

    # r = re.compile("|".join(INTAB))
    # replaces_dict = dict(zip(INTAB, OUTTAB))

    check = {"Trong", "Ngoài"}

    check_address= {
        "TRUNG QUỐC",
        "DAI LOAN",
        "TOKYO",
        "HONGKONG",
        "HONG KONG",
        "MACAO",
        "CHÂU ÂU",
        "NAM PHI",
        'Tây Ban Nha',
        "MAURITIUS",
        "NAM NINH",
        "MOSCOW",
        "MÔNG CỔ",
        "HY LẠP",
        "THÁI LAN",
        "ĐÀI LOAN",
        "ẤN ĐỘ",
        "DUBAI",
        "MAROCCO",
        "THỔ NHĨ KỲ",
        "ISRAEL",
        "CUBA",
        "MAURITUS",
        "KENYA",
        "CANADA",
        "NAM MỸ",
        "ĐAN MẠCH",
        "BHUTAN",
        "NEW ZEALAND",
        "SIBERIA",
        "TRIỀU TIÊN",
        "SRILANKA",
        "ÚC",
        "NEW YORK",
        "singapore",
        "MALAYSIA",
        "CAMPUCHIA",
        "THÁI LAN",
        "BANGKOK",
        "ĐÔNG ÂU",
        "AI CẬP",
        "JEJU",
        "ANH",
        "NGA",
        "THIÊN MÔN SƠN",
        "MALDIVES",
        "HÀN QUỐC",
        "TÂY TẠNG",
        "NHẬT BẢN",
        "HOKKAIDO"
    }

    @staticmethod
    def parse_type(string, url, name):
        
        stringNew = str.upper(string)
        for i in check:
            tmp = stringNew.find(str.upper(i))
            if tmp == -1:
                continue
            else:
                return i+" Nước"

        urlNew = str.upper(url)
        urlNew = urlNew.replace("-", " ").replace("/", " ")
        for i in check:
            if i == "Ngoài":
                tmp = urlNew.find(str.upper("Ngoai"))
            else:
                tmp = urlNew.find(str.upper(i))

            if tmp == -1:
                continue
            else:
                return i+" Nước"

        nameNew = str.upper(name)
        nameNew = nameNew.replace(":", "")
        for i in check_address:
            tmp = nameNew.find(str.upper(i))
            if tmp == -1:
                continue
            else:
                return "Ngoài Nước"
        return None

    def process_item(self, item, spider):
        item['type_tour'] = self.parse_type(item['type_tour'], item['url_tour'], item['name_tour'])
        return item

class NormalizeCostTourPipeline(object):

    @staticmethod
    def parse_cost_tour(cost, number):
        if cost is None:
           return cost
        else:
            if number is not None:
                numberNew = number.replace('/', ' ')
                tmp = numberNew.find('VNĐ')
                if tmp == -1:
                    tmp = cost.replace('.', '').replace(',', '')
                    for s in tmp.split():
                        if s.isdigit():
                            return s
                else:
                    tmp = number.replace('.', '').replace(',', '')
                    for s in tmp.split():
                        if s.isdigit():
                            return s
        return None

    def process_item(self, item, spider):
        item['cost_tour'] = self.parse_cost_tour(item['cost_tour'], item['number_date'])
        return item

class NormalizeStartDatePipeline(object):

    @staticmethod
    def parse_start_date(date):
        if date is None:
           return date
        else:
            tmp = date.split(' ')
            for i in tmp:
                check = i.find('/')
                if check == -1:
                    continue
                else:
                    if i.find(',') != -1:
                        iNew = i.split(",")
                        for k in iNew:
                            if k.find('/') != -1:
                                i = k

                    if i.count('/') == 1:
                        return i+"/2019"
                    else:
                        return i
        return None

    def process_item(self, item, spider):
        item['start_date'] = self.parse_start_date(item['start_date'])
        return item

class DuplicatesPipeline(object):
    def __init__(self):
        self.urls = set()

    def process_item(self, item, spider):
        
        if item['source'] == 'vietT':
            if item['link'] in self.urls:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.urls.add(item['link'])
                return item
        else:
            if item['url_tour'] in self.urls:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.urls.add(item['url_tour'])
                return item

class DuplicatesListPipeline(object):
    def __init__(self):
        self.jaro_winkler = JaroWinkler()
        self.list_check = list()

    def process_item(self, item, spider):
    
            name_tour = item['name_tour']
            url_tour = item['url_tour']
            number_date = item['number_date']
            if number_date is None:
                number_date = ''
            start_date = item['start_date']
            if start_date is None:
                start_date = ''

            check = name_tour + url_tour + str(number_date) + start_date

            list_new = self.list_check
            score = 0

            for value in list_new:
                name_tour_new = value['name_tour']
                if name_tour_new is None:
                    name_tour_new = ''
                url_tour_new = value['url_tour']
                number_date_new = value['number_date']
                if number_date_new is None:
                    print(type(number_date_new))
                    number_date_new = ''
                start_date_new = value['start_date']
                if start_date_new is None:
                    start_date_new = ''

                check_new = name_tour_new + url_tour_new + str(number_date_new) + start_date_new


                score =  self.jaro_winkler.similarity(check, check_new)

                if score >= 0.85:
                    print("SCORE: " + score)
                    
                    raise DropItem("Duplicate item found ")
                else:
                    self.list_check.append(item)
                    return item

            if len(list_new) == 0:
                self.list_check.append(item)
                return item

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('test1.json', 'a')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

class MongoPipeline(object):

    collection_name = 'travel'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'travel_db')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if item["number_date"] is not None:
            item["number_date"] = int(item["number_date"])
        if item["cost_tour"] is not None:
            item["cost_tour"] = int(item["cost_tour"])

        result = self.db[self.collection_name].find({ "url_tour": item["url_tour"]}).count()

        if result != 0:
            myquery = { "url_tour": item["url_tour"] }
            newvalues = { "$set": dict(item) }
            self.db[self.collection_name].update_one(myquery, newvalues)
        else:
            self.db[self.collection_name].insert_one(dict(item))
        return item