
def video_rec(question_num):
	import numpy as np
	import cv2
	from time import sleep
	duration = 15
	cap = cv2.VideoCapture(0)

	# Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('C:/Users/Arbing/Desktop/Code/video/video'+str(question_num)+ '.avi',fourcc, 20.0, (640,480))

	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret==True:
			#frame = cv2.flip(frame,0)

			# write the flipped frame
			out.write(frame)

			cv2.imshow('frame',frame)
			#sleep(duration)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			break

	# Release everything if job is finished
	cap.release()
	out.release()
	cv2.destroyAllWindows()