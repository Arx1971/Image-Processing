import numpy as np
import matplotlib.pyplot as plt
import cv2
import statistics


def calculate_histogram(source, bands):
    row, col = source.shape[0:2]
    histogram = np.zeros(256)
    for i in range(row):
        for j in range(col):
            vector = source[i, j]
            if bands == 3:
                average = (int(vector[0]) + int(vector[1]) + int(vector[2])) / 3
                histogram[int(average)] += 1
            else:
                histogram[vector[bands]] += 1

    return np.array(histogram)


def plot_histogram(img_matrix):
    color = ('r', 'g', 'b', 'k')
    for i in range(0, len(color)):
        hist = calculate_histogram(img_matrix, i)
        plt.plot(hist, color=color[i])

    plt.show()


under_exposed = cv2.imread("underexpose.jpg")
plot_histogram(under_exposed)

over_exposed = cv2.imread("overexpose.jpg")
plot_histogram(over_exposed)