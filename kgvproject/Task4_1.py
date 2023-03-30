import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = imread("Cat.jpg") #зчитування зображення
red = img[:, :, 0] #значення матриці яскравості для червоного
green = img[:, :, 1] #значення матриці яскравості для зеленого
blue = img[:, :, 2] #значення матриці яскравості для синього
brightness_matrix = (0.3 * red) + (0.59 * green) + (0.11 * blue)
brightness_matrix = brightness_matrix.astype(int)

part1 = brightness_matrix <= 128
part2 = brightness_matrix > 128
img_copy = img.copy()
img_copy[part1] = 0
img_copy[part2] = 255
plt.imshow(img_copy)

plt.axis("off") #вимкнення осей
plt.suptitle('Task 4\n Бінаризація') #визначення заголовків
plt.show()