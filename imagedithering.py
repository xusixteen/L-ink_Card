import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

filename = 'img/' + 'sunwukong2'
print(filename)
#img_gray0 = cv2.imread("img/ym_j_M.jpg", cv2.IMREAD_GRAYSCALE)
img_gray0 = cv2.imread(filename + '.jpg', cv2.IMREAD_GRAYSCALE)
img_gray0 = 255 - img_gray0
h, w= img_gray0.shape
#img_gray0 = cv2.resize(img_gray0, (w//2, h//2))
img_gray0 = cv2.resize(img_gray0, (w, h))
h, w= img_gray0.shape
#plt.figure()
#plt.imshow(img_gray0, vmin=0, vmax=255, cmap=plt.get_cmap("Greys"))
#plt.title("原图")

img_gray_eq = img_gray0
img_dither = np.zeros((h+1, w+1), dtype=np.float)
img_undither = np.zeros((h, w), dtype=np.uint8)
threshold = 128
for i in range(h):
    for j in range(w):
        img_dither[i, j] = img_gray_eq[i, j]
        if img_gray_eq[i, j] > threshold:
            img_undither[i, j] = 255
for i in range(h):
    for j in range(w):
        old_pix = img_dither[i, j]
        if (img_dither[i, j] > threshold):
            new_pix = 255
        else:
            new_pix = 0
        img_dither[i,j] = new_pix
        quant_err = old_pix - new_pix
        if j > 0:
            img_dither[i+1, j-1] = img_dither[i+1, j-1] + quant_err * 3 / 16
            img_dither[i+1, j] = img_dither[i+1, j] + quant_err * 5 / 16
            img_dither[i, j+1] = img_dither[i, j+1] + quant_err * 7 / 16
            img_dither[i+1, j+1] = img_dither[i+1, j+1] + quant_err * 1 / 16
img_dither = img_dither.astype(np.uint8)
img_dither = img_dither[0:h, 0:w]
#plt.figure()
plt.imshow(img_dither, vmin=0, vmax=255, cmap=plt.get_cmap("Greys"))
plt.axis('off')
#plt.title("dither")
#plt.figure()
#plt.imshow(img_undither, vmin=0, vmax=255, cmap=plt.get_cmap("Greys"))
#plt.title("undither")
plt.imsave(filename + '.png',img_dither)
#plt.savefig(filename + '.png')
#plt.show()
