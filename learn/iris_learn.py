from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.cm as cm

if __name__ == '__main__':
    df = pd.read_csv('iris.csv')
    df.columns = ['sepal_len', 'sepal_width', 'petal_len', 'petal_width', 'class']
    df.head(5)
    df['class'] = df['class'].apply(lambda x: x.split('-')[1])

    def scatter_plot_by_category(feat, x, y):
        alpha = 0.5
        gs = df.groupby(feat)
        cs = cm.rainbow(np.linspace(0, 1, len(gs)))
        for g, c in zip(gs, cs):
            plt.scatter(g[1][x], g[1][y], color=c, alpha=alpha)


    plt.figure(figsize=(20, 5))

    plt.subplot(131)
    scatter_plot_by_category('class', 'sepal_len', 'petal_len')
    plt.xlabel('sepal_len')
    plt.ylabel('petal_len')
    plt.title('class')
    plt.show()
