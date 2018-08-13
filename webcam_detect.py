#!/usr/bin/env python2
import cv2
import os
import sys
import numpy as np
sys.path.append('.')
import tensorflow as tf
import detect_face_detection
import time, shutil


def main():
    if os.path.exists("images_raw"):
        shutil.rmtree("images_raw")

    os.mkdir('images_raw')
    # Capture device. Usually 0 will be webcam and 1 will be usb cam.
    filename_video = 'video.mp4' #Replace with Filename here of Video kept in /uploads Folder
    file_name = os.getcwd() + "\\uploads\\" + filename_video
    video_capture = cv2.VideoCapture(file_name)
    video_capture.set(3, 640)
    video_capture.set(4, 480)

    minsize = 25 # minimum size of face
    threshold = [ 0.6, 0.7, 0.7 ]  # three steps's threshold
    factor = 0.709 # scale factor


    # sess = tf.Session()
    # sess = tf.Session() #Add GPU Module here
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.50)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
    with sess.as_default():
        pnet, rnet, onet = detect_face_detection.create_mtcnn(sess, None)
        def getFrame(sec):
            video_capture.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            # hasFrames,image = vidcap.read()
            ret, frame = video_capture.read()
            if not ret:
                return ret
            # Display the resulting frame
            img = frame[:,:,0:3]
            boxes, _ = detect_face_detection.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
            for i in range(boxes.shape[0]):
                pt1 = (int(boxes[i][0]), int(boxes[i][1]))
                pt2 = (int(boxes[i][2]), int(boxes[i][3]))
                x = int(boxes[i][0])
                y = int(boxes[i][1])
                w = int(boxes[i][2])
                h = int(boxes[i][3])
                # cv2.imshow('Video', frame)
                p1 = int(boxes[0][2])
                p2 = int(boxes[0][3])
                if ret:
                    if(float(boxes[i][4]) >= 0.95):
                        cv2.rectangle(frame, (x,y), (w, h), color=(0, 255, 0))
                        sub_faces = frame[y:h, x:w]
                        # sub_faces = frame[p1, p2]
                        path = os.getcwd() + "\\images_raw\\face_" + str(time.time()) + ".jpg"
                        cv2.imwrite(path, sub_faces)
                        # cv2.imwrite("frame "+str(sec)+" sec.jpg", image)     # save frame as JPG file
            return ret
        sec = 0
        frameRate = 0.1 #it will capture image in each 0.5 second
        success = getFrame(sec)
        while success:
            sec = sec + frameRate
            sec = round(sec, 2)
            success = getFrame(sec)
        # while(True):
        #     # vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        #     ret, frame = video_capture.read()
        #     if not ret:
        #         break
        #     # Display the resulting frame
        #     img = frame[:,:,0:3]
        #     boxes, _ = detect_face_detection.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
        #     print(boxes)
        #     for i in range(boxes.shape[0]):
        #         pt1 = (int(boxes[i][0]), int(boxes[i][1]))
        #         pt2 = (int(boxes[i][2]), int(boxes[i][3]))
        #         x = int(boxes[i][0])
        #         y = int(boxes[i][1])
        #         w = int(boxes[i][2])
        #         h = int(boxes[i][3])
        #         if(float(boxes[i][4]) >= 0.95):
        #             cv2.rectangle(frame, (x,y), (w, h), color=(0, 255, 0))
        #             sub_faces = frame[y:h, x:w]

                    
                    
        #             # sub_faces = frame[p1, p2]
        #             path = os.getcwd() + "\\images_raw\\face_" + str(time.time()) + ".jpg"
        #             cv2.imwrite(path, sub_faces)
        #     cv2.imshow('Video', frame)
            # p1 = int(boxes[0][2])
            # p2 = int(boxes[0][3])
            
            
            

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    video_capture.release()
    cv2.destroyAllWindows()




if __name__ == '__main__':
    main()
