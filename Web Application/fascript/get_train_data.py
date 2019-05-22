import cv2
import os,sys
import time

vidcap = cv2.VideoCapture(0)
success,image = vidcap.read()
count = 0
cwd = os.getcwd()
user_name = 'ABC'
dir = cwd + '/train_img/' + user_name
if not os.path.exists(dir):
    os.makedirs(dir)
success = True
while success and count!=50:
	print(count)
	time.sleep(0.75)
	success,image = vidcap.read()
	#     cv2.imshow('img',image)
	print(cv2.imwrite("train_img/"+user_name+"/frame%d.jpg" % count, image))     # save frame as JPEG file
	print('Read a new frame: ', success)
	count += 1
else:
    vidcap.release()
    cv2.destroyAllWindows()
    pass