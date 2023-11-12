# В данном примере необходимо установить все требуемые библиотеки для работы программы

import cv2  # pip install opencv-pythonimport os

frame_path = "video.mp4"  # путь к видео
cap = cv2.VideoCapture(frame_path)  # Загружаем видео

# Создайте вычитатель фона, чтобы изолировать движущиеся объекты
detector = cv2.createBackgroundSubtractorMOG2()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Преобразуйте кадр в оттенки серого
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Примените пороговое значение для захвата белых элементов
    _, binaryFrame = cv2.threshold(grayFrame, 254, 255, cv2.THRESH_BINARY)

    # Найдите контуры в двоичном кадре
    contours, _ = cv2.findContours(binaryFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Выполните итерацию по контурам и обработайте их как объекты
    for contour in contours:

        area = cv2.contourArea(contour)
        if area > 100:
            # Обработайте контур как объект
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Отобразить обработанный кадр
    cv2.imshow('video', frame)

    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

# Отпустите захват и уничтожьте все открытые окна
cap.release()
cv2.destroyAllWindows()
