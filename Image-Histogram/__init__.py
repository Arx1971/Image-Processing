import numpy as np
import matplotlib.pyplot as plt
import cv2
import PIL
from spectral import *
import math
from laspy.file import File
import matplotlib.pyplot as plt
import matplotlib as mpl

np.seterr(divide='ignore')


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

    matrix[:, :, 0] = source_image[:, :, 3]
    matrix[:, :, 1] = source_image[:, :, 2]
    matrix[:, :, 2] = source_image[:, :, 1]

    return np.array(matrix, dtype=np.uint8)


def ndvi_image_processing(source_image):
    ndvi_image = ((source_image[:, :, 3] - source_image[:, :, 2]) / (
            source_image[:, :, 3] + source_image[:, :, 2]))
    return np.array(np.uint8(ndvi_image * 255))


def color_image_from_ndvi_image(source_image):
    row, col = source_image.shape[0:2]
    color_image = np.zeros((row, col, 3))

    R = 255 * abs(np.cos((source_image * 2 * math.pi) / 255))
    G = 255 * abs(np.cos((source_image * 2 * math.pi) / 255))
    B = 255 * abs(np.cos((source_image * 2 * math.pi) / 255))

    color_image[:, :, 0] = R
    color_image[:, :, 1] = G
    color_image[:, :, 2] = B

    return np.array(np.uint8(color_image))


def hyperspectral_image():
    img = open_image('TIPJUL1.LAN')
    img = img.load()
    arr = np.array(img)
    matrix = false_image_processing(arr)
    img_1 = PIL.Image.fromarray(matrix, 'RGB')
    img_1.save('hyperspectral_image.png')
    arr = np.array(img)
    ndvi_image = ndvi_image_processing(arr)
    img_2 = PIL.Image.fromarray(ndvi_image, 'L')
    img_2.save('ndvi.png')
    ndvi_gray_scale_img = np.array(ndvi_image)
    arr = color_image_from_ndvi_image(ndvi_gray_scale_img)
    img_3 = PIL.Image.fromarray(arr, 'RGB')
    img_3.save('color_ndvi.png')


def raster_of_the_lidar_image():
    las_file = File("17258975.las")
    las_min = las_file.header.min
    las_max = las_file.header.max

    longitude = []
    latitude = []
    altitude = []

    for x, y, z, ite, c, nr, rn in np.nditer([las_file.x, las_file.y, las_file.z,
                                              las_file.Intensity, las_file.Classification,
                                              las_file.num_returns, las_file.return_num]):
        longitude.append(x)
        latitude.append(y)
        altitude.append(z)

    img_col = int((las_max[0] - las_min[0]) / 8)
    img_row = int((las_max[1] - las_min[1]) / 8)

    img = np.zeros((img_row, img_col))

    for i in range(len(latitude)):
        px = int((longitude[i] - las_min[0]) * ((img_col - 1) / (las_max[0] - las_min[0])))
        py = int((latitude[i] - las_min[1]) * ((img_row - 1) / (las_max[1] - las_min[1])))
        img[px, py] = altitude[i]

    binary_image = np.array(img, dtype=np.uint8)
    img = PIL.Image.fromarray(binary_image)
    img.save('raster_image.png')
    img.show()
    img.close()


# histogram()
# generate_binary_image()
# hyperspectral_image()
# raster_of_the_lidar_image()

# im_gray = cv2.imread("color_ndvi.png", cv2.IMREAD_GRAYSCALE)
# im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)
# plt.imshow
