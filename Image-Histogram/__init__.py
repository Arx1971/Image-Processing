import numpy as np
import matplotlib.pyplot as plt
import cv2
import PIL
from spectral import *


def calculate_histogram(source, bands):
    width, height = source.shape[0:2]
    histogram = np.zeros(256)
    for i in range(height):
        for j in range(width):
            vector = source[j, i]
            if bands == 3:
                average = (int(vector[0]) + int(vector[1]) + int(vector[2])) / 3
                histogram[int(average)] += 1
            else:
                histogram[vector[bands]] += 1

    return np.array(histogram)


def plot_histogram(img_matrix, plot_title):
    color = ('r', 'g', 'b', 'k')
    for i in range(0, len(color)):
        hist = calculate_histogram(img_matrix, i)
        plt.plot(hist, color=color[i])

    plt.title(plot_title)
    plt.savefig(plot_title + ".png")
    plt.close()
    img = PIL.Image.open(plot_title + '.png')
    img.show()


def histogram():
    under_exposed = cv2.imread("underexpose.jpg")
    plot_histogram(under_exposed, "underexposed_plot")
    over_exposed = cv2.imread("overexpose.jpg")
    plot_histogram(over_exposed, "overexposed_plot")


def image_subtraction(uniform_img, nonuniform_img, threshold):
    width, height = uniform_img.shape[0:2]
    binary = np.zeros((width, height))
    for i in range(height):
        for j in range(width):
            vector = abs(int(uniform_img[j, i]) - int(nonuniform_img[j, i]))
            if vector > threshold:
                binary[j, i] = 100
    return np.array(binary, dtype=np.uint8)


def generate_binary_image():
    uniform_scene = cv2.imread("uniform_scene.jpg", 0)
    nonuniform_scene = cv2.imread("nonuniform_scene.jpg", 0)
    binary = image_subtraction(uniform_scene, nonuniform_scene, 100)
    img = PIL.Image.fromarray(binary)
    img.save('binary_image.png')
    img.show()
    img.close()


def false_image_processing(source_image):
    width, height = source_image.shape[0:2]
    matrix = np.zeros((width, height))
    for i in range(height):
        for j in range(width):
            matrix[j, i] = source_image[j, i]

    return np.array(matrix, dtype=np.uint8)

# Problem 1
# histogram()
# Problem 2
# generate_binary_image()
# # Problem 3
# img = open_image("TIPJUL1.LAN")
# data = img.load()
# matrix = false_image_processing(data)
# img = PIL.Image.fromarray(matrix)
# img.save('image.png')
# img.show()
