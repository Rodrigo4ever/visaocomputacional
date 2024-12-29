import cv2
import mediapipe as mp
import math

video = cv2.VideoCapture('ANEXO+polichinelos.mp4')
pose = mp.solutions.pose
Pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
draw = mp.solutions.drawing_utils
contador = 0
check = True

while True:
    c, img = video.read()

    if not c:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        print("Reiniciando")
        continue

    videoRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Pose.process(videoRGB)
    points = results.pose_landmarks

    draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    h, w, _ = img.shape

    if points:
        try:
                      # Calcular coordenadas ajustadas
            peDy = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].y * h)
            peDx = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].x * w)
            peEy = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].y * h)
            peEx = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].x * w)
            moEy = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y * h)
            moEx = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x * w)
            moDy = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].y * h)
            moDx = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].x * w)

            # Calcular distâncias
            distanciaMaos = math.hypot(moDx - moEx, moDy - moEy)
            distanciaPes = math.hypot(peDx - peEx, peDy - peEy)

            if check == True and distanciaMaos <= 150 and distanciaPes >=150:
                contador +=1
                check = False
            else:
                # distanciaMaos <= 150 and distanciaPes >= 150:
                # contador += 1
                check = True
            print(contador)


        except Exception as e:
            print(f"Erro ao calcular distâncias: {e}")

    cv2.imshow('Resultado',img)
    cv2.waitKey(40)
