import cv2
import pickle

img = cv2.imread("estacionamento.png")

vagas = []

for x in range(69):
    vaga = cv2.selectROI("Mapeie a vaga", img, False)
    cv2.destroyWindow('Mapeie a vaga')
    vagas.append((vaga))

    x, y, l, a = vaga
    cv2.rectangle(img, (x, y), (x + l, y + a), (0, 0, 255), 2)

with open('vagas.pkl', 'wb') as arquivo:
    pickle.dump(vagas, arquivo)
