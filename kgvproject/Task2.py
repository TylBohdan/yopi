import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = imread("Cat.jpg") #зчитування зображення
plt.axis("off") #вимкнення осей
red = img[:, :, 0] #значення матриці яскравості для червоного
green = img[:, :, 1] #значення матриці яскравості для зеленого
blue = img[:, :, 2] #значення матриці яскравості для синього
brightness_matrix = (0.3 * red) + (0.59 * green) + (0.11 * blue)
brightness_matrix = brightness_matrix.astype(int)
plt.text(0.25, 0.8, 'Матриця яскравості:')
plt.text(0.25, 0.45, str(brightness_matrix))
plt.suptitle('Task 2') #визначення заголовків
plt.show()