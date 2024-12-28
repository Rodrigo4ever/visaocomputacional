import cv2

camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 420)
camera.set(10, 400)

while True:
    ret, frame = camera.read()

    # Se o frame for lido com sucesso
    if not ret:
        break

    frame_resized = cv2.resize(frame, (480, 380))  # Diminui o tamanho da imagem (campo de visão mais amplo)

    cv2.imshow('Camera - Zoom Longe', frame_resized)

    # Saindo ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
