import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = imread("Cat.jpg") #зчитування зображення

img_ = img / 255
img_gray = img_ @ [0.3, 0.59, 0.11]
negative_img = 1 - img_gray
plt.imshow(negative_img, cmap='gray')

plt.axis("off") #вимкнення осей
plt.suptitle('Task 4\n Негатив') #визначення заголовків
plt.show()