import cv2

classificador = cv2.CascadeClassifier('cascade.xml')

camera = cv2.VideoCapture(1)

while True:
    check, img = camera.read()
    imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    objs = classificador.detectMultiScale(imgCinza, scaleFactor=1.2)

    if len(objs) == 0:
        pass
    if len(objs) != 0:
        for (x, y, l, a) in objs:
            cv2.rectangle(img, (x,y), (x+l, y+a), (0,0,255), 2)

    cv2.imshow('Camera', img)
    cv2.waitKey(1)