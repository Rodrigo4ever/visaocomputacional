import cv2

# CORTAR UMA IMAGEM - DIRETAMENTE
# img = cv2.imread("farol.jpg");
# # imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY);
# recorte = img[310:520, 120:420];
# cv2.imshow('ImageWindow', img);
# cv2.imshow('ImageWindow2', recorte);
# cv2.waitKey(0);

# CORTAR UMA IMAGEM - USANDO PY
img = cv2.imread("farol.jpg");
dimensoes = cv2.selectROI('Selecione', img, False)
cv2.destroyWindow("Selecione");

# Desempacotando as coordenadas da ROI
v1, v2, v3, v4 = map(int, dimensoes)
recorte = img[v2:v2 + v4, v1:v1 + v3]

diretorio = "recortes/";
nome_arquivo = input('Escolha o nome');

cv2.imwrite(f"{diretorio}{nome_arquivo}.jpg", recorte);
print("Imagem salva");
# Exibir a imagem original e a imagem recortada
# cv2.imshow('Imagem Recortada', recorte)  # Exibe somente o recorte
# cv2.waitKey(0)  # Aguarda a interação do usuário (pressionando qualquer tecla)
# cv2.destroyAllWindows()  # Fecha todas as janelas abertas








# IMAGEM
# img = cv2.imread("farol.jpg");
# imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY);
# #print(img.shape);
# print(img);
# cv2.imshow('ImageWindow', img);
# cv2.imshow('ImageWindow2', imgCinza);
# cv2.waitKey(0);
#

# VIDEO
# video = cv2.VideoCapture("runners.mp4");
#
# while True:
#     check, img = video.read()
#     imgRedim = cv2.resize(img, (640,420))
#     cv2.imshow('video', imgRedim)
#     cv2.waitKey(10)

# # ABRINDO WEBCAM
# camera = cv2.VideoCapture(0);
# camera.set(3, 640)
# camera.set(4, 420)
# camera.set(10, 200)
# while True:
#     check, img = camera.read()
#     cv2.imshow('Web Cam', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break