import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = imread("Cat.jpg") #зчитування зображення
plt.axis("off") #вимкнення осей
plt.imshow(img) #вивід зображення
plt.suptitle('Task 1') #визначення заголовків
plt.show()