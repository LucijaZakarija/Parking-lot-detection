from collections import OrderedDict
from ultralytics import YOLO
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image


model = YOLO("best.pt")  # pretrained
video = cv2.VideoCapture('nepomicniTest.mp4')  # 0 iz kamere, 
while video.isOpened():
    # Procitaj frame iz videa
    success, frame = video.read()

    if success:

        print("Read a new frame: ", success)

        # primjeni yolo8
        results = model.predict(frame)

        # Vizualizacija rezultata
        annotated_frame = results[0].plot()

        # Prikaz u prozoru
        cv2.imshow(
            "YOLOv8 Inference", annotated_frame
        )  # cv2.imshow() is disabled in Colab, because it causes Jupyter sessions to crash, tako da se ovo pokrece lokalno annotated_frame
        if cv2.waitKey(1) == ord("q"):
            break
    else:
        # Ako je kraj videa ili klik na q
        break


# zatvori prozor
video.release()
cv2.destroyAllWindows()
