import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = imread("Cat.jpg") #зчитування зображення

img_ = img/255
img_gray = img_ @ [0.3, 0.59, 0.11]

hist_ = img_gray.flatten()
plt.hist(x = hist_, bins=256, color='gray', label='перехід до відтінків сірого') #побудова гістрограми переходу до відтінків сірого

plt.legend(loc='best') #лагенда
plt.suptitle('Task 4\n Гістрограма переходу до відтінків сірого') #визначення заголовків
plt.show()