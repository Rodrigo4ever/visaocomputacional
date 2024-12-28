import cv2

video = cv2.VideoCapture('runners.mp4')

while True:
    check, img = video.read()

    if not check:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Voltar para o início do vídeo
        print('Reiniciando o video')
        continue  # Começar o loop novamente


    cv2.rectangle(img, (50,50), (200,200), (255,125,255), 3)
    cv2.circle(img, (200,200), 50, (255, 100, 255), 5)
    cv2.line(img, (300,400),(500, 300), (0, 0, 255), 2)
    cv2.putText(img, 'texto', (300, 250), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 200), 2)

    imgRedim = cv2.resize(img, (640, 420))
    cv2.imshow('video', imgRedim)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# img = cv2.imread('piramide.jpg')
#
# cv2.rectangle(img, (50,50), (200,200), (255,125,255), 3)
# cv2.circle(img, (200,200), 50, (255, 100, 255), 5)
# cv2.line(img, (300,400),(500, 300), (0, 0, 255), 2)
# texto = 'Piramides Egito';
#
# cv2.putText(img, texto, (300, 250), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 200), 2)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)