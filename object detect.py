import cv2
import numpy as np
# from ex_images1 import ver_aero
# from ex_images1 import ver_bi
# from ex_images1 import ver_bird
# from ex_images1 import ver_bo
# from ex_images1 import ver_bot
# from ex_images1 import ver_bus
# from ex_images2 import ver_car
# from ex_images2 import ver_cat
# from ex_images2 import ver_chair
# from ex_images2 import ver_cow
# from ex_images3 import ver_tab
# from ex_images2 import ver_dog
# from ex_images2 import ver_hos
# from ex_images3 import ver_mtb
# from ex_images3 import ver_psn
# from ex_images3 import ver_pln
# from ex_images3 import ver_shp
# from ex_images3 import ver_sofa
# from ex_images4 import ver_trn
# from ex_images34 import ver_tvm

CLASSES = ["BACKGROUND", "AEROPLANE", "BICYCLE", "BIRD", "BOAT",
           "BOTTLE", "BUS", "CAR", "CAT", "CHAIR", "COW", "TABLE",
           "DOG", "HORSE", "MOTORBIKE", "PERSON", "PLANT", "SHEEP",
           "SOFA", "TRAIN", "TVMONITOR"]

COLORS = np.random.uniform(0,255,size=(len(CLASSES),3))

net = cv2.dnn.readNetFromCaffe("./MobileNetSSD_deploy/MobileNetSSD_deploy.prototxt",
                               "./MobileNetSSD_deploy/MobileNetSSD_deploy.caffemodel")

class_index = []

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('test1/images/a3a0e5eb23500231bfbf0790d6d7c4aa.jpg')
#cap = cv2.VideoCapture('test1/f1e1ef9e734702eb91718e976b335d05.jpg')

while True:
    ret, frame = cap.read()
    if ret:
        (h,w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame,
                                     0.007843,
                                     (300,300),
                                     127.5)
        net.setInput(blob)

        detections = net.forward()

        for i in np.arange(0, detections.shape[2]):
            percent = detections[0,0,i,2]
            if percent > 0.5:
                class_inedx = int(detections[0,0,i,1])
                box = detections[0,0,i,3:7]*np.array([w,h,w,h])
                (startX, startY, endX, endY) = box.astype("int")

                label = "{} [{:.2f}%]".format(CLASSES[class_inedx],
                                              percent*100)

                cv2.rectangle(frame,
                              (startX,startY),
                              (endX,endY),
                              COLORS[class_inedx],
                              2)

                y = startY-15 if startY-15>15 else startY+15

                cv2.putText(frame,
                            label,
                            (startX+20, y+5),
                            cv2.FONT_HERSHEY_DUPLEX,
                            0.6,
                            (255,255,255),
                            1)

        cv2.imshow("Frame", frame)
        #if ["AEROPLANE"]:
            #cv2.imshow("Aeroplane", ver_aero)

        #elif detections == ["BICYCLE"]:
            #cv2.imshow("Bicycle", ver_bi)

        #elif detections == ["BIRD"]:
            #cv2.imshow("Bird", ver_bird)

        #elif detections == ["BOAT"]:
            #cv2.imshow("Boat", ver_bo)

        #elif detections == ["BOTTLE"]:
            #cv2.imshow("Bottle", ver_bot)

        #elif detections == ["BUS"]:
            #cv2.imshow("Bus", ver_bus)

        #elif detections == ["CAR"]:
            #cv2.imshow("Car", ver_car)

        #elif detections == ["CAT"]:
            #cv2.imshow("Cat", ver_cat)

        #elif detections == ["CHAIR"]:
           # cv2.imshow("Chair", ver_chair)

        #elif detections == ["COW"]:
            #cv2.imshow("Cow", ver_cow)

        #elif detections == ["TABLE"]:
            #cv2.imshow("Table", ver_tab)

        #elif detections == ["DOG"]:
            #cv2.imshow("Dog", ver_dog)

        #elif detections == ["HORSE"]:
            #cv2.imshow("Horse", ver_hos)

        #elif detections == ["MOTORBIKE"]:
            #cv2.imshow("Motorbike", ver_mtb)

        #elif detections == ["PERSON"]:
            #cv2.imshow("Person", ver_psn)

        #elif detections == ["PLANT"]:
            #cv2.imshow("Plant", ver_pln)

        #elif detections == ["SHEEP"]:
            #cv2.imshow("Sheep", ver_shp)

        #elif detections == ["SOFA"]:
            #cv2.imshow("Sofa", ver_sofa)

        #elif detections == ["TRAIN"]:
            #cv2.imshow("Train", ver_trn)

        #elif detections == ["TVMONITOR"]:
            #cv2.imshow("TV Monitor", ver_tvm)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
