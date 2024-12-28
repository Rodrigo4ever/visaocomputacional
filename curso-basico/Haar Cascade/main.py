import cv2

# video1 = cv2.VideoCapture(0)  # Primeira câmera
# video2 = cv2.VideoCapture(1)  # Segunda câmera

video1 = cv2.VideoCapture('video.mp4')  # Primeira câmera

# camera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier('cascades/haarcascade_fullbody.xml')

while True:
    check1, img1 = video1.read()
    # check2, img2 = video2.read()

    # Verificar se as câmeras estão funcionando corretamente
    if not check1:
        print("Falha na captura de vídeo.")
        break
    # Converter para escala de cinza para o classificador Haar
    img1Gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    # img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    #
    # Detectar os olhos na imagem 1
    objetos1 = classificador.detectMultiScale(img1Gray, minSize=(50, 50), scaleFactor=1.5)
    for x, y, l, a in objetos1:
        cv2.rectangle(img1, (x, y), (x + l, y + a), (0, 0, 255), 2)

    # Detectar os olhos na imagem 2
    # objetos2 = classificador.detectMultiScale(img2Gray, minSize=(50, 50), scaleFactor=8.1)
    # for x, y, l, a in objetos2:
    #     cv2.rectangle(img2, (x, y), (x + l, y + a), (0, 0, 255), 2)

    # Redimensionar as imagens para uma exibição melhor
    img1Redim = cv2.resize(img1, (640, 400))
    # img2Redim = cv2.resize(img2, (640, 400))

    # Exibir as imagens em duas janelas diferentes
    cv2.imshow('WebCam 1', img1Redim)
    # cv2.imshow('WebCam 2', img2Redim)

    # Pressionar 'q' para sair do loop
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Libera as câmeras e fecha as janelas
video1.release()
# video2.release()
cv2.destroyAllWindows()