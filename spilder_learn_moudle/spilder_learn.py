# -*- coding: utf-8 -*-
import json
import random
import time
import uuid
import requests
from bs4 import BeautifulSoup


class House(object):
    # __slots__ = 'title', 'price', 'area', 'type', 'location', 'img_href', 'page_url'

    def __init__(self, title, price, area, type, location, img_href, page_url):
        self.title = title
        self.price = price
        self.area = area
        self.type = type
        self.location = location
        self.img_href = img_href
        self.page_url = page_url


def get_house_list(search_page_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    html = requests.get(search_page_url,
                        headers=headers)
    bs = BeautifulSoup(html.text, features='html.parser')
    house_list = bs.find('ul', {'class': 'listUl'})
    house_list = house_list.find_all('li')
    for house in house_list:
        if '月' in str(house):
            title = str(house.find('div', {'class': 'des'}).find('h2').find('a').text).replace(' ', '').replace('\n',
                                                                                                                '')
            pic_url = str(house.find('div', {'class': 'img_list'}).find('a').find('img').get('lazy_src')).replace('//',
                                                                                                                  'https://')
            page_url = str(house.find('div', {'class': 'des'}).find('h2').find('a').get('href')).replace('//',
                                                                                                         'https://')
            location = str(house.find('div', {'class': 'des'}).find('p', {'class': 'add'}).find('a').text).replace('\n',
                                                                                                                   '')
            price = house.find('div', {'class', 'money'}).find('b').text

            type_and_area = str(house.find('p', {'class': 'room strongbox'}).text).replace(
                '                            ', '|').split('|')
            house_type = type_and_area[0]
            house_area = str(type_and_area[1]).split('㎡')[0]
            if not str(price).isdigit():
                continue
            if not str(house_area).isdigit():
                continue

            price = float(price)
            house_area = float(house_area)

            house_item = House(title, price, house_area, house_type, location, pic_url, page_url)
            info = json.dumps(house_item, default=lambda obj: obj.__dict__).encode('utf-8').decode('unicode_escape')
            # download_pic(pic_url)

            with open('C:/Users/Administrator/Desktop/houses.txt', 'a', encoding='utf-8') as f:
                f.writelines(info + '\n')


def download_pic(pic_url):
    pic_req = requests.get(pic_url)
    with open('C:/Users/Administrator/Desktop/pic/' + str(uuid.uuid4()) + '.png', 'wb') as f:
        f.write(pic_req.content)


if __name__ == '__main__':
    for i in range(1, 71):
        time.sleep(random.randint(0, 2))
        get_house_list('https://bj.58.com/zufang/pn' + str(i) + '/')
        print('进度%f' % ((i * 100.0) / 70))
