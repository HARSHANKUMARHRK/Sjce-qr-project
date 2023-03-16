import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from PIL import Image

cap = cv2.VideoCapture(0)
imm=False
font = cv2.FONT_HERSHEY_PLAIN
while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    imm=False
    if imm==False:
     for obj in decodedObjects:
        img= str(obj.data).replace("b","")
        img= img.replace("'","")
        print(str(obj.data).replace("b",""))
        imge = "/home/kishore/Pictures/sjce_ponnunga/"+img+".JPG"
        # img = cv2.imread(imge, cv2.IMREAD_ANYCOLOR)
        image = Image.open(imge)
        image.show()
        imm=True
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)
        
