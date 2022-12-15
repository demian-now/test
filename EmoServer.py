import socket
import os
from fer import FER
import matplotlib.pyplot as plt


def detect_emo(data):
    img_path = data.decode()
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    test_image_one = plt.imread(img_path)
    emo_detector = FER(mtcnn=True)
    captured_emotions = emo_detector.detect_emotions(test_image_one)
    #print(captured_emotions)
    return captured_emotions


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 3030))  # Привязываем серверный сокет к localhost и 3030 порту.
s.listen(1)  # Начинаем прослушивать входящие соединения.
conn, addr = s.accept()  # Метод который принимает входящее соединение.

while True:
    data = conn.recv(1024)  # Получаем данные из сокета.
    #print(data)
    if not data:
        break
    #print(data)
    send = detect_emo(data)
    s = ''.join(str(x) for x in send)
    print(s)
    conn.sendall(s.encode()) # Отправляем данные в сокет.

conn.close()
