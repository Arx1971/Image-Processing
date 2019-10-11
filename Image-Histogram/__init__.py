import numpy as np
import matplotlib.pyplot as plt
import cv2
import PIL
from spectral import *
from laspy.file import File


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
    row, col = source_image.shape[0:2]
    matrix = np.zeros((row, col, 3))
    for i in range(row):
        for j in range(col):
            matrix[i, j, 0] = source_image[i, j, 3]
            matrix[i, j, 1] = source_image[i, j, 2]
            matrix[i, j, 2] = source_image[i, j, 1]

    return np.array(matrix, dtype=np.uint8)


def hyperspectral_image():
    img = open_image('TIPJUL1.LAN')
    img = img.load()
    arr = np.array(img)
    matrix = false_image_processing(arr)
    img = PIL.Image.fromarray(matrix, 'RGB')
    img.save('hyperspectral_image.png')


histogram()
generate_binary_image()
hyperspectral_image()