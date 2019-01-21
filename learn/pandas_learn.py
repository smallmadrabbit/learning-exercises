# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt


def load_data():
    with open('C:/Users/Administrator/Desktop/User.data', 'r', encoding='utf-8') as f:
        years = {}
        exception_count = 0
        file_data = f.readlines()
        for line in file_data:
            try:
                check = int(line.split("|")[4])
                # if check != 1:
                #     continue
                date_str = line.split("|")[13].split(" ")[0].split("/")
                year = int(date_str[0])
                month = int(date_str[1])
                if year not in years:
                    months = {x: 0 for x in range(1, 13)}
                    years[year] = months
                years[year][month] += 1
            except Exception as e:
                exception_count += 1
                continue
        print('无法处理的数据', exception_count)
        return years


if __name__ == '__main__':
    data = load_data()
    plt.figure()
    count = 0
    user_count = 0
    for year in data:
        user_count = user_count + sum(data[year].values())
        print('%d年新增用户总数%s'% (year, sum(data[year].values())))
        last_point = []
        x = list(data[year].keys())
        y = list(data[year].values())
        for month in x:
            # print(month, data[year][month])
            current_point = [month, data[year][month]]
            if len(last_point):
                color = 'k'
                if year == 2014:
                    # 绿色
                    color = 'lawngreen'
                if year == 2015:
                    # 亮蓝
                    color = 'cyan'
                if year == 2016:
                    # 红色
                    color = 'r'
                if year == 2017:
                    # 紫色
                    color = 'fuchsia'
                if year == 2018:
                    # 蓝色
                    color = 'blue'
                if year == 2019:
                    color = 'slategray'
                print_x = [last_point[0], current_point[0]]
                print_y = [last_point[1], current_point[1]]
                plt.plot(print_x, print_y, color=color, linestyle='--')
            last_point = current_point
    print(user_count)
    plt.show()
