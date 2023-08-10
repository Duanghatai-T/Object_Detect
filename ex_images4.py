import cv2
import numpy as np

# train-TV
scale = 0.8
h, w = 200,200

# train
img_trn1 = cv2.imread('classesimg/train/2f326ab2a3e987943b3a99bf74019e1e.jpg')
img_trn1 = cv2.resize(img_trn1, (h, w), None, scale, scale)

img_trn2 = cv2.imread('classesimg/train/5fe0580dd2c8d5a76666760405e2de0a.jpg')
img_trn2 = cv2.resize(img_trn2, (h, w), None, scale, scale)

img_trn3 = cv2.imread('classesimg/train/71642df3a7bbacabb83b7b7ac2b745e6.jpg')
img_trn3 = cv2.resize(img_trn3, (h, w), None, scale, scale)

img_trn4 = cv2.imread('classesimg/train/740e925bb2143a2ab11b28b716c126af.jpg')
img_trn4 = cv2.resize(img_trn4, (h, w), None, scale, scale)

img_trn5 = cv2.imread('classesimg/train/8bc6f685afd8a3467b1055bf916decfb.jpg')
img_trn5 = cv2.resize(img_trn5, (h, w), None, scale, scale)

img_trn6 = cv2.imread('classesimg/train/d98db64cb6db78dab1c032591bc4badc.jpg')
img_trn6 = cv2.resize(img_trn6, (h, w), None, scale, scale)

img_trn7 = cv2.imread('classesimg/train/dcdb879b12d897f6053a188b6121662f.jpg')
img_trn7 = cv2.resize(img_trn7, (h, w), None, scale, scale)

img_trn8 = cv2.imread('classesimg/train/e5e4e8da735fa2110701e15a9d15ad59.jpg')
img_trn8 = cv2.resize(img_trn8, (h, w), None, scale, scale)

img_trn9 = cv2.imread('classesimg/train/ebdba5bb3a4bd2fe86e89106a51317bb.jpg')
img_trn9 = cv2.resize(img_trn9, (h, w), None, scale, scale)

hor = np.hstack((img_trn1, img_trn2, img_trn3,))
hor2 = np.hstack((img_trn4, img_trn5, img_trn6))
hor3 = np.hstack((img_trn7, img_trn8, img_trn9))
ver_trn = np.vstack((hor, hor2, hor3))

cv2.imshow("Train", ver_trn)

# TV
img_tvm1 = cv2.imread('classesimg/tvmonitor/23ebdce293f5e329a601c1e1e0b1673e.jpg')
img_tvm1 = cv2.resize(img_tvm1, (h, w), None, scale, scale)

img_tvm2 = cv2.imread('classesimg/tvmonitor/25cd6bc38dfb5d156c1b4cf55be874ac.jpg')
img_tvm2 = cv2.resize(img_tvm2, (h, w), None, scale, scale)

img_tvm3 = cv2.imread('classesimg/tvmonitor/342aee691bca84d8c7eca6fd73040b18.jpg')
img_tvm3 = cv2.resize(img_tvm3, (h, w), None, scale, scale)

img_tvm4 = cv2.imread('classesimg/tvmonitor/80be91bf0daefd962b8ba9e8238f7920.jpg')
img_tvm4 = cv2.resize(img_tvm4, (h, w), None, scale, scale)

img_tvm5 = cv2.imread('classesimg/tvmonitor/82bd53e3c8661ba742453af803a930a4.jpg')
img_tvm5 = cv2.resize(img_tvm5, (h, w), None, scale, scale)

img_tvm6 = cv2.imread('classesimg/tvmonitor/9219f4883ca400a3992a825a9f4fb1cd.jpg')
img_tvm6 = cv2.resize(img_tvm6, (h, w), None, scale, scale)

img_tvm7 = cv2.imread('classesimg/tvmonitor/aeea5942dded5d49cc1d5352fe4a0588.jpg')
img_tvm7 = cv2.resize(img_tvm7, (h, w), None, scale, scale)

img_tvm8 = cv2.imread('classesimg/tvmonitor/be92a836e7d24a3bc30e1ddab031bf6e.jpg')
img_tvm8 = cv2.resize(img_tvm8, (h, w), None, scale, scale)

img_tvm9 = cv2.imread('classesimg/tvmonitor/f37601ddb7e5daf01cab1c4d01644d5c.jpg')
img_tvm9 = cv2.resize(img_tvm9, (h, w), None, scale, scale)

hor = np.hstack((img_tvm1, img_tvm2, img_tvm3,))
hor2 = np.hstack((img_tvm4, img_tvm5, img_tvm6))
hor3 = np.hstack((img_tvm7, img_tvm8, img_tvm9))
ver_tvm = np.vstack((hor, hor2, hor3))

cv2.imshow("TV Monitor", ver_tvm)