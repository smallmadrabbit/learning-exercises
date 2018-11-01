# -*- coding: utf-8 -*-
from contextlib import closing

from bs4 import BeautifulSoup
import requests
import json


class ProgressBar(object):

    def __init__(self, title,
                 count=0.0,
                 run_status=None,
                 fin_status=None,
                 total=100.0,
                 unit='', sep='/',
                 chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "【%s】%s %.2f %s %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.statue)
        self.unit = unit
        self.seq = sep

    def __get_info(self):
        # 【名称】状态 进度 单位 分割线 总数 单位
        _info = self.info % (self.title, self.status,
                             self.count / self.chunk_size, self.unit, self.seq, self.total / self.chunk_size, self.unit)
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        # if status is not None:
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        print(self.__get_info(), end=end_str)


if __name__ == '__main__':
    data_url = 'https://data.services.jetbrains.com/products/releases?code=IIU%2CIIC&latest=true&type=release&build=&_=1541037249049'
    idea_json = requests.get(data_url).text
    # print(idea_json, type(idea_json))
    idea_data = json.loads(idea_json)
    # 更新日期
    update_date = idea_data['IIU'][0]['date']
    # 下载连接
    download_url = idea_data['IIU'][0]['downloads']['windows']['link']
    # 文件大小
    size = idea_data['IIU'][0]['downloads']['windows']['size']
    file_name = str(download_url).split("/")[-1]
    with closing(requests.get(download_url, stream=True)) as response:
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 内容体总大小
        progress = ProgressBar(file_name, total=content_size,
                               unit='KB', chunk_size=chunk_size, run_status='正在下载', fin_status='下载完成')
        with open('./' + str(download_url).split('/')[-1], 'wb') as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                progress.refresh(count=len(data))
