import cv2
vidcap = cv2.VideoCapture('velikiParking.mp4') #vidi treba li path
success,image = vidcap.read()
count = 0
fps = vidcap.get(cv2.CAP_PROP_FPS)
print('frames per second =',fps)
while success: #smanji broj fps za vecu razliku 
  if count%29==0:
    cv2.imwrite("/velikiParking%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
