import cv2

video = cv2.VideoCapture(1)
amostra = 1

while True:
    check, img = video.read()
    imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        imgR = cv2.resize(imgCinza, (200,200))
        cv2.imwrite(f'fotos/p/im-{amostra}.jpg', imgR)
        amostra += 1

    cv2.imshow('Captura', img)
    cv2.waitKey(1)