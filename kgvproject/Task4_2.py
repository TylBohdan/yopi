import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = imread("Cat.jpg") #зчитування зображення

img_ = img/255
img_gray = img_ @ [0.3, 0.59, 0.11]
plt.imshow(img_gray, cmap='gray')

plt.axis("off") #вимкнення осей
plt.suptitle('Task 4\n перехід до відтінків сірого') #визначення заголовків
plt.show()