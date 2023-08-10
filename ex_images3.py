import cv2
import numpy as np

# motorbike
img_mtb1 = cv2.imread('classesimg/motorbike/5e7937b7ee66c567ea39021f908fd2a2.jpg')
img_mtb1 = cv2.resize(img_mtb1, (h, w), None, scale, scale)

img_mtb2 = cv2.imread('classesimg/motorbike/198db6c805927dddd9deff4628e77eed.jpg')
img_mtb2 = cv2.resize(img_mtb2, (h, w), None, scale, scale)

img_mtb3 = cv2.imread('classesimg/motorbike/623fd44a4554e815e25dc9098760b206.jpg')
img_mtb3 = cv2.resize(img_mtb3, (h, w), None, scale, scale)

img_mtb4 = cv2.imread('classesimg/motorbike/ac9aa5c9a9722884bf1a7c75b7a9bc01.jpg')
img_mtb4 = cv2.resize(img_mtb4, (h, w), None, scale, scale)

img_mtb5 = cv2.imread('classesimg/motorbike/ad2070daafc497eaf1f8ff9c1a810cd0.jpg')
img_mtb5 = cv2.resize(img_mtb5, (h, w), None, scale, scale)

img_mtb6 = cv2.imread('classesimg/motorbike/ca050e75e848876b515bf39982fe6e46.jpg')
img_mtb6 = cv2.resize(img_mtb6, (h, w), None, scale, scale)

img_mtb7 = cv2.imread('classesimg/motorbike/ce66869b7a743ab009abe634ace0a932.jpg')
img_mtb7 = cv2.resize(img_mtb7, (h, w), None, scale, scale)

img_mtb8 = cv2.imread('classesimg/motorbike/d013d53f38fd366fd42512a1a29f3c88.jpg')
img_mtb8 = cv2.resize(img_mtb8, (h, w), None, scale, scale)

img_mtb9 = cv2.imread('classesimg/motorbike/f63144d6eb3446608a757d38c95ecfb9.jpg')
img_mtb9 = cv2.resize(img_mtb9, (h, w), None, scale, scale)

hormtb = np.hstack((img_mtb1, img_mtb2, img_mtb3,))
hormtb2 = np.hstack((img_mtb4, img_mtb5, img_mtb6))
hormtb3 = np.hstack((img_mtb7, img_mtb8, img_mtb9))
ver_mtb = np.vstack((hormtb, hormtb2, hormtb3))


# person
img_psn1 = cv2.imread('classesimg/person/1ffbb585a7fda0b8fc47bc648d1b513c.jpg')
img_psn1 = cv2.resize(img_psn1, (h, w), None, scale, scale)

img_psn2 = cv2.imread('classesimg/person/2b19c0d0cdd2e417ab0cfee8ba86a0ae.jpg')
img_psn2 = cv2.resize(img_psn2, (h, w), None, scale, scale)

img_psn3 = cv2.imread('classesimg/person/07b465a1c007172af505deb35f431862.jpg')
img_psn3 = cv2.resize(img_psn3, (h, w), None, scale, scale)

img_psn4 = cv2.imread('classesimg/person/23bdfdb8e0d89f3eb33ef4f3642fa539.jpg')
img_psn4 = cv2.resize(img_psn4, (h, w), None, scale, scale)

img_psn5 = cv2.imread('classesimg/person/a2f8365e0c9c91a24ffa288166d53476.jpg')
img_psn5 = cv2.resize(img_psn5, (h, w), None, scale, scale)

img_psn6 = cv2.imread('classesimg/person/cf6ec445df41899479978aa16f05c996.jpg')
img_psn6 = cv2.resize(img_psn6, (h, w), None, scale, scale)

img_psn7 = cv2.imread('classesimg/person/e9bea136174ea8047de1a7b8f4f6dbfb.jpg')
img_psn7 = cv2.resize(img_psn7, (h, w), None, scale, scale)

img_psn8 = cv2.imread('classesimg/person/e6d441fe5998affaf7d6a6591b3f4d3e.jpg')
img_psn8 = cv2.resize(img_psn8, (h, w), None, scale, scale)

img_psn9 = cv2.imread('classesimg/person/fc9de80da08a4e4f57199ccc16228f2b.jpg')
img_psn9 = cv2.resize(img_psn9, (h, w), None, scale, scale)

horpsn = np.hstack((img_psn1, img_psn2, img_psn3,))
horpsn2 = np.hstack((img_psn4, img_psn5, img_psn6))
horpsn3 = np.hstack((img_psn7, img_psn8, img_psn9))
ver_psn = np.vstack((horpsn, horpsn2, horpsn3))


# plant
img_pln1 = cv2.imread('classesimg/plant/5cc8f6b072eb36c67072fa3a6e8a3353.jpg')
img_pln1 = cv2.resize(img_pln1, (h, w), None, scale, scale)

img_pln2 = cv2.imread('classesimg/plant/84f8a53a14b53ad45071e32dc9245b64.jpg')
img_pln2 = cv2.resize(img_pln2, (h, w), None, scale, scale)

img_pln3 = cv2.imread('classesimg/plant/117ed8ea8f9b95969e455bd2bfc1c117.jpg')
img_pln3 = cv2.resize(img_pln3, (h, w), None, scale, scale)

img_pln4 = cv2.imread('classesimg/plant/5463d8f3fec7850a09fb8b6d8bd8d16c.jpg')
img_pln4 = cv2.resize(img_pln4, (h, w), None, scale, scale)

img_pln5 = cv2.imread('classesimg/plant/273170e674d9b4d5507d604b1f539032.jpg')
img_pln5 = cv2.resize(img_pln5, (h, w), None, scale, scale)

img_pln6 = cv2.imread('classesimg/plant/715721cef5bcf33a255a0b5480e27d1e.jpg')
img_pln6 = cv2.resize(img_pln6, (h, w), None, scale, scale)

img_pln7 = cv2.imread('classesimg/plant/b096b61653a7d341018a8d2cc7ceedcf.jpg')
img_pln7 = cv2.resize(img_pln7, (h, w), None, scale, scale)

img_pln8 = cv2.imread('classesimg/plant/c3984598eccb3ec732450216a168f6a8.jpg')
img_pln8 = cv2.resize(img_pln8, (h, w), None, scale, scale)

img_pln9 = cv2.imread('classesimg/plant/fe3d5922d4108d0aec18d51986a4b215.jpg')
img_pln9 = cv2.resize(img_pln9, (h, w), None, scale, scale)

horpln = np.hstack((img_pln1, img_pln2, img_pln3,))
horpln2 = np.hstack((img_pln4, img_pln5, img_pln6))
horpln3 = np.hstack((img_pln7, img_pln8, img_pln9))
ver_pln = np.vstack((horpln, horpln2, horpln3))


# sheep
img_shp1 = cv2.imread('classesimg/sheep/16eb9503058df6af25014c4017a2655c.jpg')
img_shp1 = cv2.resize(img_shp1, (h, w), None, scale, scale)

img_shp2 = cv2.imread('classesimg/sheep/1b8d233ac44e8ff4306db36aecd5051f.jpg')
img_shp2 = cv2.resize(img_shp2, (h, w), None, scale, scale)

img_shp3 = cv2.imread('classesimg/sheep/2ed8b5a312eed59d9bdeaee5b5f00ed0.jpg')
img_shp3 = cv2.resize(img_shp3, (h, w), None, scale, scale)

img_shp4 = cv2.imread('classesimg/sheep/356f2ca69c7c30a4c5c351c6b9e265b6.jpg')
img_shp4 = cv2.resize(img_shp4, (h, w), None, scale, scale)

img_shp5 = cv2.imread('classesimg/sheep/4e2d5601222c3e2633f717e36f5b662e.jpg')
img_shp5 = cv2.resize(img_shp5, (h, w), None, scale, scale)

img_shp6 = cv2.imread('classesimg/sheep/c64b56acb638c0498694564dfcb83ecb.jpg')
img_shp6 = cv2.resize(img_shp6, (h, w), None, scale, scale)

img_shp7 = cv2.imread('classesimg/sheep/ca106004d8dd76bec74e9cbfc99ef0bf.jpg')
img_shp7 = cv2.resize(img_shp7, (h, w), None, scale, scale)

img_shp8 = cv2.imread('classesimg/sheep/cb56f819130e6dd95faa9bda7c8469e9.jpg')
img_shp8 = cv2.resize(img_shp8, (h, w), None, scale, scale)

img_shp9 = cv2.imread('classesimg/sheep/d9eac6f8fd4dbd34fed31349253c08f7.jpg')
img_shp9 = cv2.resize(img_shp9, (h, w), None, scale, scale)

horshp = np.hstack((img_shp1, img_shp2, img_shp3,))
horshp2 = np.hstack((img_shp4, img_shp5, img_shp6))
horshp3 = np.hstack((img_shp7, img_shp8, img_shp9))
ver_shp = np.vstack((horshp, horshp2, horshp3))


# sofa
img_sofa1 = cv2.imread('classesimg/sofa/0b7bed3709399ae80b17a5c6b6e2647c.jpg')
img_sofa1 = cv2.resize(img_sofa1, (h, w), None, scale, scale)

img_sofa2 = cv2.imread('classesimg/sofa/0e0a26e94dae017dd41ca5780929ca29.jpg')
img_sofa2 = cv2.resize(img_sofa2, (h, w), None, scale, scale)

img_sofa3 = cv2.imread('classesimg/sofa/02dac7ae52e14088380b82234c2e71cb.jpg')
img_sofa3 = cv2.resize(img_sofa3, (h, w), None, scale, scale)

img_sofa4 = cv2.imread('classesimg/sofa/4659f7e1182f94a5f0134303d32e96d9.jpg')
img_sofa4 = cv2.resize(img_sofa4, (h, w), None, scale, scale)

img_sofa5 = cv2.imread('classesimg/sofa/59cb93d1b9b99eb653e09f013e1fa9f2.jpg')
img_sofa5 = cv2.resize(img_sofa5, (h, w), None, scale, scale)

img_sofa6 = cv2.imread('classesimg/sofa/6dcc2a3c05bf30a1b5a51ac642dc641c.jpg')
img_sofa6 = cv2.resize(img_sofa6, (h, w), None, scale, scale)

img_sofa7 = cv2.imread('classesimg/sofa/7238131c3b8ffb857abec0a1778d526c.jpg')
img_sofa7 = cv2.resize(img_sofa7, (h, w), None, scale, scale)

img_sofa8 = cv2.imread('classesimg/sofa/948f47471245139499fcfa1ed79309be.jpg')
img_sofa8 = cv2.resize(img_sofa8, (h, w), None, scale, scale)

img_sofa9 = cv2.imread('classesimg/sofa/ba517bdcd7849a820cc3a8b9fff1c06e.jpg')
img_sofa9 = cv2.resize(img_sofa9, (h, w), None, scale, scale)

horsofa = np.hstack((img_sofa1, img_sofa2, img_sofa3,))
horsofa2 = np.hstack((img_sofa4, img_sofa5, img_sofa6))
horsofa3 = np.hstack((img_sofa7, img_sofa8, img_sofa9))
ver_sofa = np.vstack((horsofa, horsofa2, horsofa3))


# table
img_tab1 = cv2.imread('classesimg/table/4a024774eeb75e6adb8a65737f7cc03e.jpg')
img_tab1 = cv2.resize(img_tab1, (h, w), None, scale, scale)

img_tab2 = cv2.imread('classesimg/table/12eb0c45d4a16b779786baf7d4055f2c.jpg')
img_tab2 = cv2.resize(img_tab2, (h, w), None, scale, scale)

img_tab3 = cv2.imread('classesimg/table/74a9925fb382e2a011d9e0f074ed9133.jpg')
img_tab3 = cv2.resize(img_tab3, (h, w), None, scale, scale)

img_tab4 = cv2.imread('classesimg/table/b1ed01ffb32c49c839ac474bc6c7abec.jpg')
img_tab4 = cv2.resize(img_tab4, (h, w), None, scale, scale)

img_tab5 = cv2.imread('classesimg/table/b21a645ed04a2f903a9732e617746eb8.jpg')
img_tab5 = cv2.resize(img_tab5, (h, w), None, scale, scale)

img_tab6 = cv2.imread('classesimg/table/b0269cad5a2e80b86db335f8033d3c91.jpg')
img_tab6 = cv2.resize(img_tab6, (h, w), None, scale, scale)

img_tab7 = cv2.imread('classesimg/table/bd3ef837aa7ca674dbf5200654e4f8f9.jpg')
img_tab7 = cv2.resize(img_tab7, (h, w), None, scale, scale)

img_tab8 = cv2.imread('classesimg/table/c87a633c125f2973f8b67f390a7b045a.jpg')
img_tab8 = cv2.resize(img_tab8, (h, w), None, scale, scale)

img_tab9 = cv2.imread('classesimg/table/c4654888459cff672e0053d73b49cdec.jpg')
img_tab9 = cv2.resize(img_tab9, (h, w), None, scale, scale)

hortab = np.hstack((img_tab1, img_tab2, img_tab3,))
hortab2 = np.hstack((img_tab4, img_tab5, img_tab6))
hortab3 = np.hstack((img_tab7, img_tab8, img_tab9))
ver_tab = np.vstack((hortab, hortab2, hortab3))

cv2.imshow("Table", ver_tab)
cv2.waitKey()
