import cv2
from time import sleep

# Abrir archivo de video
cap = cv2.VideoCapture('video_pr.mp4')

# Ancho y alto del video
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Code para archivo de video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Archivo de salida
# 30 --> fps
out = cv2.VideoWriter('new_video.mp4', fourcc, 30, (w,h))

# Mostrar todo el video
for i in range(150): # revisar que el video esté abierto
    ret, img = cap.read()
    # revisar que haya más frames
    if ret == False:
        break
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(gray, (3,3), 0)
    edges = cv2.Canny(image=img_blur, threshold1=10, threshold2=200)
    edges_and = cv2.bitwise_and(img, img, mask=edges)
    cv2.imshow('imagen',edges_and)
    # gravación del video
    out.write(edges_and)
    
    # Salida con tecla ESC
    if cv2.waitKey(1) == 27:
        break
    
    sleep(1/30)