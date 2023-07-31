import cv2
import datetime

class Camera:
    def __init__(self):
        self.stream = cv2.VideoCapture(0)
    def take_photo(self):
        ret, frame = self.stream.read()
        cv2.imwrite(datetime.datetime.now().strftime('%d-%m-%Y %H-%M') + '.jpg', img=frame)

camera = Camera()
camera.take_photo()
