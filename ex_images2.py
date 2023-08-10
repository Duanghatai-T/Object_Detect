import cv2
import numpy as np

# car-horse
scale = 0.8
h, w = 200,200

#car
img_car1 = cv2.imread('classesimg/car/2eafa59f7b3ca901784b55614c89a0e3.jpg')
img_car1 = cv2.resize(img_car1, (h, w), None, scale, scale)

img_car2 = cv2.imread('classesimg/car/7ab40753833f60e988de043b5cfa29cf.jpg')
img_car2 = cv2.resize(img_car2, (h, w), None, scale, scale)

img_car3 = cv2.imread('classesimg/car/8c30a5a398fc0c24c51f1868d2e179dd.jpg')
img_car3 = cv2.resize(img_car3, (h, w), None, scale, scale)

img_car4 = cv2.imread('classesimg/car/8f7606c389a23ffe853074e55cea536e.jpg')
img_car4 = cv2.resize(img_car4, (h, w), None, scale, scale)

img_car5 = cv2.imread('classesimg/car/9e897e988d8bd6928f3526fd7050aa02.jpg')
img_car5 = cv2.resize(img_car5, (h, w), None, scale, scale)

img_car6 = cv2.imread('classesimg/car/0431b85e40b9625e941d3b9e478dbc6b.jpg')
img_car6 = cv2.resize(img_car6, (h, w), None, scale, scale)

img_car7 = cv2.imread('classesimg/car/472a4363ed9e165ae57869b39502cffa.jpg')
img_car7 = cv2.resize(img_car7, (h, w), None, scale, scale)

img_car8 = cv2.imread('classesimg/car/538a54c1c8e4511fb9a73d170cbe76b0.jpg')
img_car8 = cv2.resize(img_car8, (h, w), None, scale, scale)

img_car9 = cv2.imread('classesimg/car/d9c1f324bc6a3b8bef2170ef8560a8dd.jpg')
img_car9 = cv2.resize(img_car9, (h, w), None, scale, scale)

hor = np.hstack((img_car1, img_car2, img_car3,))
hor2 = np.hstack((img_car4, img_car5, img_car6))
hor3 = np.hstack((img_car7, img_car8, img_car9))
ver_car = np.vstack((hor, hor2, hor3))

cv2.imshow("Car", ver_car)

# cat


img_cat1 = cv2.imread('classesimg/cat/0cb1fadd58cb6cd40b3c37147f467f6b.jpg')
img_cat1 = cv2.resize(img_cat1, (h, w), None, scale, scale)

img_cat2 = cv2.imread('classesimg/cat/8cee528dffb6bd8a8ff625c8c324426c.jpg')
img_cat2 = cv2.resize(img_cat2, (h, w), None, scale, scale)

img_cat3 = cv2.imread('classesimg/cat/9eaaa6c9edd85a632351e246e44291b0.jpg')
img_cat3 = cv2.resize(img_cat3, (h, w), None, scale, scale)

img_cat4 = cv2.imread('classesimg/cat/37fc6b1698a99cd5d03e7e984c968ef6.jpg')
img_cat4 = cv2.resize(img_cat4, (h, w), None, scale, scale)

img_cat5 = cv2.imread('classesimg/cat/50a8cc7d92c6c72bc7812625d6e65486.jpg')
img_cat5 = cv2.resize(img_cat5, (h, w), None, scale, scale)

img_cat6 = cv2.imread('classesimg/cat/241ec5ae44ce4951cfd7b11d60099723.jpg')
img_cat6 = cv2.resize(img_cat6, (h, w), None, scale, scale)

img_cat7 = cv2.imread('classesimg/cat/8728bceccd7a5bc8ec136d1b79f6d4cc.jpg')
img_cat7 = cv2.resize(img_cat7, (h, w), None, scale, scale)

img_cat8 = cv2.imread('classesimg/cat/f0c254940a1e0cb7713da9daee2ba08a.jpg')
img_cat8 = cv2.resize(img_cat8, (h, w), None, scale, scale)

img_cat9 = cv2.imread('classesimg/cat/f2a1fc70c27557433d62d6b7f7b6b4e6.jpg')
img_cat9 = cv2.resize(img_cat9, (h, w), None, scale, scale)

hor = np.hstack((img_cat1, img_cat2, img_cat3,))
hor2 = np.hstack((img_cat4, img_cat5, img_cat6))
hor3 = np.hstack((img_cat7, img_cat8, img_cat9))
ver_cat = np.vstack((hor, hor2, hor3))

cv2.imshow("Cat", ver_cat)

# chair
img_chair1 = cv2.imread('classesimg/chair/6c8f923fd440d8c71a6ab40b1dbe4556.jpg')
img_chair1 = cv2.resize(img_chair1, (h, w), None, scale, scale)

img_chair2 = cv2.imread('classesimg/chair/11aaee0caff9fcd25070b6686fce6d6a.jpg')
img_chair2 = cv2.resize(img_chair2, (h, w), None, scale, scale)

img_chair3 = cv2.imread('classesimg/chair/25d7853973359d9cc7a492dfa72132e5.jpg')
img_chair3 = cv2.resize(img_chair3, (h, w), None, scale, scale)

img_chair4 = cv2.imread('classesimg/chair/220d4e4912c40221d8c0515638c886c8.jpg')
img_chair4 = cv2.resize(img_chair4, (h, w), None, scale, scale)

img_chair5 = cv2.imread('classesimg/chair/b62f627496cc42518234de363e5e2f8f.jpg')
img_chair5 = cv2.resize(img_chair5, (h, w), None, scale, scale)

img_chair6 = cv2.imread('classesimg/chair/bf57225790ce18343257ee84a4c83044.jpg')
img_chair6 = cv2.resize(img_chair6, (h, w), None, scale, scale)

img_chair7 = cv2.imread('classesimg/chair/c88c1286c09a9687a82007b32662fdfe.jpg')
img_chair7 = cv2.resize(img_chair7, (h, w), None, scale, scale)

img_chair8 = cv2.imread('classesimg/chair/c933ceea7069682e022dd40601b006b3.jpg')
img_chair8 = cv2.resize(img_chair8, (h, w), None, scale, scale)

img_chair9 = cv2.imread('classesimg/chair/fde4ccc8b5bea141d4387f1ba3b26088.jpg')
img_chair9 = cv2.resize(img_chair9, (h, w), None, scale, scale)

hor = np.hstack((img_chair1, img_chair2, img_chair3,))
hor2 = np.hstack((img_chair4, img_chair5, img_chair6))
hor3 = np.hstack((img_chair7, img_chair8, img_chair9))
ver_chair = np.vstack((hor, hor2, hor3))

cv2.imshow("Chair", ver_chair)

# cow
img_cow1 = cv2.imread('classesimg/cow/3d632c45b8cb350b2577fead3c65500f.jpg')
img_cow1 = cv2.resize(img_cow1, (h, w), None, scale, scale)

img_cow2 = cv2.imread('classesimg/cow/5b865975a31a485df422247bfd433c85.jpg')
img_cow2 = cv2.resize(img_cow2, (h, w), None, scale, scale)

img_cow3 = cv2.imread('classesimg/cow/6c5f86be3c1b9aeb409ce6fac2bc0d90.jpg')
img_cow3 = cv2.resize(img_cow3, (h, w), None, scale, scale)

img_cow4 = cv2.imread('classesimg/cow/11eab5fff0406b780e0a5029caa74f99.jpg')
img_cow4 = cv2.resize(img_cow4, (h, w), None, scale, scale)

img_cow5 = cv2.imread('classesimg/cow/59002a08b4c6b7c8ba507469704bb6f4.jpg')
img_cow5 = cv2.resize(img_cow5, (h, w), None, scale, scale)

img_cow6 = cv2.imread('classesimg/cow/a31d8be7e27f3a8ffedd056456b59b1b.jpg')
img_cow6 = cv2.resize(img_cow6, (h, w), None, scale, scale)

img_cow7 = cv2.imread('classesimg/cow/c9e3f1a0c22659d792fe5198e3f05894.jpg')
img_cow7 = cv2.resize(img_cow7, (h, w), None, scale, scale)

img_cow8 = cv2.imread('classesimg/cow/f1e0a65f0aae53c42bf807441c515726.jpg')
img_cow8 = cv2.resize(img_cow8, (h, w), None, scale, scale)

img_cow9 = cv2.imread('classesimg/cow/b7364395f0436795825af2474282b629.jpg')
img_cow9 = cv2.resize(img_cow9, (h, w), None, scale, scale)

hor = np.hstack((img_cow1, img_cow2, img_cow3,))
hor2 = np.hstack((img_cow4, img_cow5, img_cow6))
hor3 = np.hstack((img_cow7, img_cow8, img_cow9))
ver_cow = np.vstack((hor, hor2, hor3))

cv2.imshow("Cow", ver_cow)

# dog
img_dog1 = cv2.imread('classesimg/dog/63ff60628078ea38501416cee19b2f65.jpg')
img_dog1 = cv2.resize(img_dog1, (h, w), None, scale, scale)

img_dog2 = cv2.imread('classesimg/dog/90c5eeb588d8d7fad288aa88a471131e.jpg')
img_dog2 = cv2.resize(img_dog2, (h, w), None, scale, scale)

img_dog3 = cv2.imread('classesimg/dog/234af48e071f85e443a447eb01de7ba3.jpg')
img_dog3 = cv2.resize(img_dog3, (h, w), None, scale, scale)

img_dog4 = cv2.imread('classesimg/dog/06125b01b5949975a898e64c32b2798f.jpg')
img_dog4 = cv2.resize(img_dog4, (h, w), None, scale, scale)

img_dog5 = cv2.imread('classesimg/dog/72386685efbc4be77c6601f2896ba598.jpg')
img_dog5 = cv2.resize(img_dog5, (h, w), None, scale, scale)

img_dog6 = cv2.imread('classesimg/dog/279774515d9c731c1b8458a1e4111fab.jpg')
img_dog6 = cv2.resize(img_dog6, (h, w), None, scale, scale)

img_dog7 = cv2.imread('classesimg/dog/ce2b477540aa57e36b9eee926b68d22c.jpg')
img_dog7 = cv2.resize(img_dog7, (h, w), None, scale, scale)

img_dog8 = cv2.imread('classesimg/dog/e6243c807215fdd39023364e849dbe59.jpg')
img_dog8 = cv2.resize(img_dog8, (h, w), None, scale, scale)

img_dog9 = cv2.imread('classesimg/dog/cf6ef9bddebbb36bdbdb288676051648.jpg')
img_dog9 = cv2.resize(img_dog9, (h, w), None, scale, scale)

hor = np.hstack((img_dog1, img_dog2, img_dog3,))
hor2 = np.hstack((img_dog4, img_dog5, img_dog6))
hor3 = np.hstack((img_dog7, img_dog8, img_dog9))
ver_dog = np.vstack((hor, hor2, hor3))

cv2.imshow("Dog", ver_dog)

# horse
img_hos1 = cv2.imread('classesimg/horse/5c32f523f35ee658ddb35383d73a27fc.jpg')
img_hos1 = cv2.resize(img_hos1, (h, w), None, scale, scale)

img_hos2 = cv2.imread('classesimg/horse/6f05c52138ac54bc80ab3147ccde951f.jpg')
img_hos2 = cv2.resize(img_hos2, (h, w), None, scale, scale)

img_hos3 = cv2.imread('classesimg/horse/8c89515152e64f81d4d2099df9f2d7ec.jpg')
img_hos3 = cv2.resize(img_hos3, (h, w), None, scale, scale)

img_hos4 = cv2.imread('classesimg/horse/8307b1d94a4cc094c7eba4e450219d40.jpg')
img_hos4 = cv2.resize(img_hos4, (h, w), None, scale, scale)

img_hos5 = cv2.imread('classesimg/horse/b4d199a563fa2f320e7331420ea91ff4.jpg')
img_hos5 = cv2.resize(img_hos5, (h, w), None, scale, scale)

img_hos6 = cv2.imread('classesimg/horse/87607debd2b69b21c4930a4f9304446c.jpg')
img_hos6 = cv2.resize(img_hos6, (h, w), None, scale, scale)

img_hos7 = cv2.imread('classesimg/horse/becc4b88e4549589fc89261663cd3cb7.jpg')
img_hos7 = cv2.resize(img_hos7, (h, w), None, scale, scale)

img_hos8 = cv2.imread('classesimg/horse/e816f2cfafa893c92f81eee80abdbdb0.jpg')
img_hos8 = cv2.resize(img_hos8, (h, w), None, scale, scale)

img_hos9 = cv2.imread('classesimg/horse/fc040d4715b4082566b2f83818cb4253.jpg')
img_hos9 = cv2.resize(img_hos9, (h, w), None, scale, scale)

hor = np.hstack((img_hos1, img_hos2, img_hos3,))
hor2 = np.hstack((img_hos4, img_hos5, img_hos6))
hor3 = np.hstack((img_hos7, img_hos8, img_hos9))
ver_hos = np.vstack((hor, hor2, hor3))

cv2.imshow("Horse", ver_hos)