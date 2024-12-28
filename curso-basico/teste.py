import cv2

video = cv2.VideoCapture()
ip = "https://192.168.137.59:8080/video"
video.open(ip)

while True:
    check, img = video.read()
    imgRedim = cv2.resize(img, (640, 400))
    cv2.imshow("img", imgRedim)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break