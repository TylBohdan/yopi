import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = imread("Cat.jpg") #зчитування зображення
red = img[:, :, 0] #значення матриці яскравості для червоного
green = img[:, :, 1] #значення матриці яскравості для зеленого
blue = img[:, :, 2] #значення матриці яскравості для синього
brightness_matrix = (0.3 * red) + (0.59 * green) + (0.11 * blue)
brightness_matrix = brightness_matrix.astype(int)

hist_ = brightness_matrix.flatten()
plt.hist(x = hist_, bins=256, color='gray', label='гістограма яскравості') #побудова загальної гістрограми яскравості

hist_r = red.flatten()
plt.hist(x = hist_r, bins=256, color='red', label='гістограма червоного') #побудова гістограми для червоного каналу

hist_g = green.flatten()
plt.hist(x = hist_g, bins=256, color='green', label='гістограма зеленого') #побудова гістограми для зеленого каналу

hist_b = blue.flatten()
plt.hist(x = hist_b, bins=256, color='blue', label='гістограма синього') #побудова гістограми для синього каналу

plt.legend(loc='best') #лагенда
plt.suptitle('Task 3') #визначення заголовків
plt.show()