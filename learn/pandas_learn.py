# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt


def load_data():
    with open('C:/Users/Administrator/Desktop/User.data', 'r', encoding='utf-8') as f:
        years = {}
        exception_count = 0
        file_data = f.readlines()
        for line in file_data:
            try:
                date_str = line.split("|")[13].split(" ")[0].split("/")
                year = int(date_str[2])
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
    for year in data:
        count += 1
        last_point = []
        x = list(data[year].keys())
        y = list(data[year].values())
        for month in x:
            # print(month, data[year][month])
            current_point = [month, data[year][month]]
            if len(last_point):
                color = 'k'
                if count == 1:
                    color = 'k'
                if count == 2:
                    color = 'r'
                if count == 3:
                    color = 'y'
                if count == 4:
                    color = 'c'
                if count == 5:
                    color = 'b'
                print_x = [last_point[0], current_point[0]]
                print_y = [last_point[1], current_point[1]]
                plt.plot(print_x, print_y, color=color,  linestyle='--')
            last_point = current_point
    plt.show()
