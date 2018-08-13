#!/usr/bin/env python2
import cv2
import os
import sys
import numpy as np
sys.path.append('.')
import tensorflow as tf
import detect_face
import time, shutil


def detect():
    if os.path.exists("images_raw"):
        shutil.rmtree("images_raw")

    os.mkdir('images_raw')
    # Capture device. Usually 0 will be webcam and 1 will be usb cam.
    video_capture = cv2.VideoCapture('video.mp4')
    video_capture.set(3, 640)
    video_capture.set(4, 480)

    minsize = 25 # minimum size of face
    threshold = [ 0.6, 0.7, 0.7 ]  # three steps's threshold
    factor = 0.709 # scale factor


    # sess = tf.Session()
    # sess = tf.Session() #Add GPU Module here
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.75)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
    with sess.as_default():
        pnet, rnet, onet = detect_face.create_mtcnn(sess, None)
        while(True):
            ret, frame = video_capture.read()
            if not ret:
                break
            # Display the resulting frame
            img = frame[:,:,0:3]
            boxes, _ = detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
            print(boxes)
            for i in range(boxes.shape[0]):
                pt1 = (int(boxes[i][0]), int(boxes[i][1]))
                pt2 = (int(boxes[i][2]), int(boxes[i][3]))
                x = int(boxes[i][0])
                y = int(boxes[i][1])
                w = int(boxes[i][2])
                h = int(boxes[i][3])
                if(float(boxes[i][4]) >= 0.95):
                    cv2.rectangle(frame, (x,y), (w, h), color=(0, 255, 0))
                    sub_faces = frame[y:h, x:w]

                    
                    
                    # sub_faces = frame[p1, p2]
                    path = os.getcwd() + "\\images_raw\\face_" + str(time.time()) + ".jpg"
                    cv2.imwrite(path, sub_faces)
            cv2.imshow('Video', frame)
            # p1 = int(boxes[0][2])
            # p2 = int(boxes[0][3])
            
            
            

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    video_capture.release()
    cv2.destroyAllWindows()




# if __name__ == '__main__':
#     main()