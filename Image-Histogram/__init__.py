import numpy as np
import matplotlib.pyplot as plt
import cv2
import statistics


def calculate_histogram(source, bands):
    row, col = under_exposed.shape[0:2]
    histogram = np.zeros(256)
    for i in range(row):
        for j in range(col):
            vector = source[i, j]
            if bands == 3:
                average = (int(vector[0])+int(vector[1])+int(vector[2]))/3
                histogram[int(average)] += 1
            else:
                histogram[vector[bands]] += 1

    return np.array(histogram)


under_exposed = cv2.imread("underexpose.jpg")

