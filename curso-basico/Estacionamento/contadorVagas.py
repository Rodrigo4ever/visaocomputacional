import cv2
import pickle

import numpy as np
from numpy.ma.core import count

vagas = []

with open('vagas.pkl', 'rb') as arquivo:
    vagas = pickle.load(arquivo)

video = cv2.VideoCapture("video.mp4")

while True:
    c, img = video.read()

    # Reiniciar o vídeo se ele atingir o final
    if not c:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        print("Reiniciando")
        continue


    imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    imgTh = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgTh, 5)
    kernel = np.ones((3,3), np.int8)
    imgDil = cv2.dilate(imgMedian, kernel)

    vagasAbertas = 0

    for x,y, l, a in vagas:
        vaga = imgDil[y:y+a, x:x+l]
        count = cv2.countNonZero(vaga)
        cv2.putText(img, str(count), (x,y+a-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 1)
        if count < 800:
            cv2.rectangle(img, (x, y), (x + l, y + a), (0, 255, 0), 2)
            vagasAbertas +=1
        else:
            cv2.rectangle(img, (x, y), (x + l, y + a), (0, 0, 255), 2)

        cv2.rectangle(img, (90,0), (310,50), (0,0,0), -1)
        cv2.putText(img, f'Livre: {vagasAbertas}/69', (95,35), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

    cv2.imshow('video', img)
    # cv2.imshow('video2', imgTh)
    cv2.waitKey(10)
