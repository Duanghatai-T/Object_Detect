import cv2
import numpy as np

# aeroplane-bus
scale = 0.8
h, w = 200,200

# aeroplane
img_aero1 = cv2.imread('classesimg/aeroplane/51958_aeroplane-1838708_1280_1.jpg')
img_aero1 = cv2.resize(img_aero1, (h, w), None, scale, scale)

img_aero2 = cv2.imread('classesimg/aeroplane/aeroplane_boeing_737_air_new_zealand_218019.jpg')
img_aero2 = cv2.resize(img_aero2, (h, w), None, scale, scale)

img_aero3 = cv2.imread('classesimg/aeroplane/Aeroplane_take-off.jpg.820x520_q95_crop-smart.jpg')
img_aero3 = cv2.resize(img_aero3, (h, w), None, scale, scale)

img_aero4 = cv2.imread('classesimg/aeroplane/Airplane_on_sky.jpg')
img_aero4 = cv2.resize(img_aero4, (h, w), None, scale, scale)
img_aero4 = cv2.cvtColor(img_aero4, cv2.COLOR_BGR2RGB)

img_aero5 = cv2.imread('classesimg/aeroplane/istockphoto-155439315-612x612.jpg')
img_aero5 = cv2.resize(img_aero5, (h, w), None, scale, scale)

img_aero6 = cv2.imread('classesimg/aeroplane/plane.jpg')
img_aero6 = cv2.resize(img_aero6, (h, w), None, scale, scale)

img_aero7 = cv2.imread('classesimg/aeroplane/plane1.jpg')
img_aero7 = cv2.resize(img_aero7, (h, w), None, scale, scale)

img_aero8 = cv2.imread('classesimg/aeroplane/pexels-pixabay-46148.jpg')
img_aero8 = cv2.resize(img_aero8, (h, w), None, scale, scale)

img_aero9 = cv2.imread('classesimg/aeroplane/pexels-pascal-borener-1089306.jpg')
img_aero9 = cv2.resize(img_aero9, (h, w), None, scale, scale)

hor = np.hstack((img_aero1, img_aero2, img_aero3,))
hor2 = np.hstack((img_aero4, img_aero5, img_aero6))
hor3 = np.hstack((img_aero7, img_aero8, img_aero9))
ver_aero = np.vstack((hor, hor2, hor3))

cv2.imshow("Aeroplane",ver_aero)

# bicycle
img_bi1 = cv2.imread('classesimg/bicycle/07b21fb0fc34308d92e2d643e69db860.jpg')
img_bi1 = cv2.resize(img_bi1, (h, w), None, scale, scale)

img_bi2 = cv2.imread('classesimg/bicycle/26dc426a933e1357b7a47f5056f4a09d.jpg')
img_bi12 = cv2.resize(img_bi2, (h, w), None, scale, scale)

img_bi3 = cv2.imread('classesimg/bicycle/596ff49ab42a023392c4c0a0beb7f961.jpg')
img_bi3 = cv2.resize(img_bi3, (h, w), None, scale, scale)

img_bi4 = cv2.imread('classesimg/bicycle/845015e355b1c8bb3e7756fe1f666e1d.jpg')
img_bi4 = cv2.resize(img_bi4, (h, w), None, scale, scale)

img_bi5 = cv2.imread('classesimg/bicycle/a53e9f71b0549ac89cdebea2ef76c5ca.jpg')
img_bi5 = cv2.resize(img_bi5, (h, w), None, scale, scale)

img_bi6 = cv2.imread('classesimg/bicycle/c371bab1df4df2e2f36885eb647aad9d.jpg')
img_bi6 = cv2.resize(img_bi6, (h, w), None, scale, scale)

img_bi7 = cv2.imread('classesimg/bicycle/c54213380160952192d11b4f8af25701.jpg')
img_bi7 = cv2.resize(img_bi7, (h, w), None, scale, scale)

img_bi8 = cv2.imread('classesimg/bicycle/f6591f2f287899dc2bdb3b8724943b65.jpg')
img_bi8 = cv2.resize(img_bi8, (h, w), None, scale, scale)

img_bi9 = cv2.imread('classesimg/bicycle/fa577f1cf62ed078fb97d213a7567934.jpg')
img_bi9 = cv2.resize(img_bi9, (h, w), None, scale, scale)

hor = np.hstack((img_bi1, img_bi2, img_bi3,))
hor2 = np.hstack((img_bi4, img_bi5, img_bi6))
hor3 = np.hstack((img_bi7, img_bi8, img_bi9))
ver_bi = np.vstack((hor, hor2, hor3))

cv2.imshow("Bicycle",ver_bi)

# bird
img_bird1 = cv2.imread('classesimg/bird/0eb52f1c6b38ad73d2758201f3a0fe2a.jpg')
img_bird1 = cv2.resize(img_bird1, (h, w), None, scale, scale)

img_bird2 = cv2.imread('classesimg/bird/10ef50fd7abcc3cb9e35aef6467ff589.jpg')
img_bird2 = cv2.resize(img_bird2, (h, w), None, scale, scale)

img_bird3 = cv2.imread('classesimg/bird/106b2f318c0b9906ec011ebb40f4b60e.jpg')
img_bird3 = cv2.resize(img_bird3, (h, w), None, scale, scale)

img_bird4 = cv2.imread('classesimg/bird/0272f8bd7e8d2a375d771fef6d16634b.jpg')
img_bird4 = cv2.resize(img_bird4, (h, w), None, scale, scale)

img_bird5 = cv2.imread('classesimg/bird/876161572e4347f114a3bb8bd1d656ff.jpg')
img_bird5 = cv2.resize(img_bird5, (h, w), None, scale, scale)

img_bird6 = cv2.imread('classesimg/bird/ccd38a51ecc3fe7a316015cc9b94db0c.jpg')
img_bird6 = cv2.resize(img_bird6, (h, w), None, scale, scale)

img_bird7 = cv2.imread('classesimg/bird/d5531638fff1e2abe2d9ae4045e1badc.jpg')
img_bird7 = cv2.resize(img_bird7, (h, w), None, scale, scale)

img_bird8 = cv2.imread('classesimg/bird/fcbd8e55707331bd9c3b9de12974084e.jpg')
img_bird8 = cv2.resize(img_bird8, (h, w), None, scale, scale)

img_bird9 = cv2.imread('classesimg/bird/fcc1b0489927b74c932d672f6790cc92.jpg')
img_bird9 = cv2.resize(img_bird9, (h, w), None, scale, scale)

hor = np.hstack((img_bird1, img_bird2, img_bird3,))
hor2 = np.hstack((img_bird4, img_bird5, img_bird6))
hor3 = np.hstack((img_bird7, img_bird8, img_bird9))
ver_bird = np.vstack((hor, hor2, hor3))

cv2.imshow("Bird", ver_bird)

# boat
img_bo1 = cv2.imread('classesimg/boat/2bb819a65d9e777680998b35bafa658a.jpg')
img_bo1 = cv2.resize(img_bo1, (h, w), None, scale, scale)

img_bo2 = cv2.imread('classesimg/boat/24d298d16e9444a0af3404926c694dce.jpg')
img_bo2 = cv2.resize(img_bo2, (h, w), None, scale, scale)

img_bo3 = cv2.imread('classesimg/boat/83c26a45721c3e635f943ad8f5496ab3.jpg')
img_bo3 = cv2.resize(img_bo3, (h, w), None, scale, scale)

img_bo4 = cv2.imread('classesimg/boat/141b5ac5d04923ae1624cdaec00531fd.jpg')
img_bo4 = cv2.resize(img_bo4, (h, w), None, scale, scale)

img_bo5 = cv2.imread('classesimg/boat/4420e2d3653c6ebb28d6515f6ecfa62e.jpg')
img_bo5 = cv2.resize(img_bo5, (h, w), None, scale, scale)
img_bo5 = cv2.cvtColor(img_bo5, cv2.COLOR_BGR2RGB)

img_bo6 = cv2.imread('classesimg/boat/0499822268f95e20d6c23d14701e9657.jpg')
img_bo6 = cv2.resize(img_bo6, (h, w), None, scale, scale)

img_bo7 = cv2.imread('classesimg/boat/a0f9aae892955c1b3ee61566fb290310.jpg')
img_bo7 = cv2.resize(img_bo7, (h, w), None, scale, scale)

img_bo8 = cv2.imread('classesimg/boat/b7628b8074fd91af13385a3c6a4273e8.jpg')
img_bo8 = cv2.resize(img_bo8, (h, w), None, scale, scale)

img_bo9 = cv2.imread('classesimg/boat/142240c5772d7c22c60f189019a121fa.jpg')
img_bo9 = cv2.resize(img_bo9, (h, w), None, scale, scale)

hor = np.hstack((img_bo1, img_bo2, img_bo3,))
hor2 = np.hstack((img_bo4, img_bo5, img_bo6))
hor3 = np.hstack((img_bo7, img_bo8, img_bo9))
ver_bo = np.vstack((hor, hor2, hor3))

cv2.imshow("Boat", ver_bo)

# bottle
img_bot1 = cv2.imread('classesimg/bottle/0b136e890bdf4406f8ff59900c4dc4c4.jpg')
img_bot1 = cv2.resize(img_bot1, (h, w), None, scale, scale)

img_bot2 = cv2.imread('classesimg/bottle/0f6759c6d743e7b0854ea5e3cc0ba0fc.jpg')
img_bot2 = cv2.resize(img_bot2, (h, w), None, scale, scale)

img_bot3 = cv2.imread('classesimg/bottle/9d34e11ec290a3c3ea4b9ca22e5bcb66.jpg')
img_bot3 = cv2.resize(img_bot3, (h, w), None, scale, scale)

img_bot4 = cv2.imread('classesimg/bottle/27dd0b2d022f2cd4ababd75add86910f.jpg')
img_bot4 = cv2.resize(img_bot4, (h, w), None, scale, scale)

img_bot5 = cv2.imread('classesimg/bottle/70a7dce394133d7ec9cf0534eb7e1eef.jpg')
img_bot5 = cv2.resize(img_bot5, (h, w), None, scale, scale)

img_bot6 = cv2.imread('classesimg/bottle/3541fbc3d5548d70dad6b0e28706cd55.jpg')
img_bot6 = cv2.resize(img_bot6, (h, w), None, scale, scale)

img_bot7 = cv2.imread('classesimg/bottle/a4155c59737259c1a36664792f8c9390.jpg')
img_bot7 = cv2.resize(img_bot7, (h, w), None, scale, scale)

img_bot8 = cv2.imread('classesimg/bottle/ceba2d930c914cd70b6f66f7ad66a1f7.jpg')
img_bot8 = cv2.resize(img_bot8, (h, w), None, scale, scale)

img_bot9 = cv2.imread('classesimg/bottle/e4a89260a46c04a9a8685edb75b07026.jpg')
img_bot9 = cv2.resize(img_bot9, (h, w), None, scale, scale)

hor = np.hstack((img_bot1, img_bot2, img_bot3,))
hor2 = np.hstack((img_bot4, img_bot5, img_bot6))
hor3 = np.hstack((img_bot7, img_bot8, img_bot9))
ver_bot = np.vstack((hor, hor2, hor3))

cv2.imshow("Boat", ver_bot)

# bus

img_bus1 = cv2.imread('classesimg/bus/5801474820ff96c525584aa1aa11679d.jpg')
img_bus1 = cv2.resize(img_bus1, (h, w), None, scale, scale)

img_bus2 = cv2.imread('classesimg/bus/0ba43386f8c1c526a2995903859fd952.jpg')
img_bus2 = cv2.resize(img_bus2, (h, w), None, scale, scale)

img_bus3 = cv2.imread('classesimg/bus/4c77acd6fd97c83588ceca5b6e18bf61.jpg')
img_bus3 = cv2.resize(img_bus3, (h, w), None, scale, scale)

img_bus4 = cv2.imread('classesimg/bus/4f7b740a36f2bbe77319c446b8dcf3ff.jpg')
img_bus4 = cv2.resize(img_bus4, (h, w), None, scale, scale)

img_bus5 = cv2.imread('classesimg/bus/4112f394bee66e7191c717845c32d637.jpg')
img_bus5 = cv2.resize(img_bus5, (h, w), None, scale, scale)

img_bus6 = cv2.imread('classesimg/bus/6c0478b34f8ce05ccf568f95e58e8565.jpg')
img_bus6 = cv2.resize(img_bus6, (h, w), None, scale, scale)

img_bus7 = cv2.imread('classesimg/bus/33a309b32ff25d45c65d0819fd8a45e4.jpg')
img_bus7 = cv2.resize(img_bus7, (h, w), None, scale, scale)

img_bus8 = cv2.imread('classesimg/bus/5138dfe75e1780f61543494040b94074.jpg')
img_bus8 = cv2.resize(img_bus8, (h, w), None, scale, scale)

img_bus9 = cv2.imread('classesimg/bus/8823a4b9201b51e1ef2cb9a99c1434df.jpg')
img_bus9 = cv2.resize(img_bus9, (h, w), None, scale, scale)

hor = np.hstack((img_bus1, img_bus2, img_bus3,))
hor2 = np.hstack((img_bus4, img_bus5, img_bus6))
hor3 = np.hstack((img_bus7, img_bus8, img_bus9))
ver_bus = np.vstack((hor, hor2, hor3))

cv2.imshow("Boat", ver_bus)