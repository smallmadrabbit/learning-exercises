# -*- coding: UTF-8 -*-
import numpy as np
from sklearn.cluster import KMeans


def load_data():
    path = "city.txt"
    fr = open(path, 'r+', encoding='utf-8')
    lines = fr.readlines()
    retData = []
    retCityName = []
    for line in lines:
        items = line.split(",")
        retCityName.append(items[0])
        for i in range(1, len(items)):
            items[i] = float(items[i])
        retData.append(items[1:])
        fr.close()
    return retData, retCityName


if __name__ == '__main__':
    data, city_name = load_data()
    n_cluster = 4
    # print(data)
    # print(city_name)
    km = KMeans(n_clusters=n_cluster)
    label = km.fit_predict(data)
    # print('聚类标签', label, len(label))
    # print('聚类中心', type(km.cluster_centers_))
    # print(km.cluster_centers_)
    expenses = np.sum(km.cluster_centers_, axis=1)
    city_cluster = [[], [], [], []]
    for i in range(len(city_name)):
        city_cluster[label[i]].append(city_name[i])
    for i in range(len(city_cluster)):
        print("Expenses:%.2f" % expenses[i])
        print(city_cluster[i])

    # print(3242.22333333 + 544.92 + 735.78 + 405.51333333 + 602.25 +  1016.62 + 760.52333333 + 446.82666667)
