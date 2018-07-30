import os
import cv2
import numpy as np
import shutil
import itertools

import face_match_demo


imageList = list()
facesList = []
writeFlag = list()
dir
clusterList = []
newImageList = list()
arr = list()

if os.path.exists("results"):
    shutil.rmtree("results")

os.mkdir('results')
def compare2face(img1,img2):
    if img1 and img2:
        # calculate Euclidean distance
        dist = np.sqrt(np.sum(np.square(np.subtract(img1[0]['embedding'], img2[0]['embedding']))))
        return dist
    return -1

for filename in os.listdir(os.getcwd()+"/images"):
    filename1 = os.getcwd()+"/images/"+str(filename)
    if '.jpg' in filename1:
        imageList.append(filename1)

# print(flagList)
for filename in imageList[:]:
    img1 = cv2.imread(filename)
    faces = face_match_demo.getFace(img1)
    if len(faces) != 0:
        # imageList.remove(filename)
        newImageList.append(filename)
        facesList.append({'filename': filename, 'faces': faces})
    else:
        print("No Faces")

if os.path.exists("my_img"):
    shutil.rmtree("my_img")

os.mkdir('my_img')

for idx, faces in enumerate(facesList):
    path = os.getcwd() + "/my_img"
    if os.path.exists("my_img"):
        shutil.copy(faces['filename'], path)
    else:
        shutil.copy(faces['filename'], path)

# print(facesList)
del imageList[:]
del facesList[:]

for filename in os.listdir(os.getcwd()+"/my_img"):
    filename1 = os.getcwd()+"/my_img/"+str(filename)
    if '.jpg' in filename1:
        imageList.append(filename1)

for filename in imageList[:]:
    img1 = cv2.imread(filename)
    faces = face_match_demo.getFace(img1)
    if len(faces) != 0:
        # imageList.remove(filename)
        # newImageList.append(filename)
        facesList.append({'filename': filename, 'faces': faces})
    else:
        print("No Faces")

for idx, face in enumerate(facesList):
    # print(face['filename'])
    if not face['filename'] in arr:
        clusterList.append([])
        for idx2, otherFaces in enumerate(facesList):
            if not otherFaces['filename'] in arr:
                distance = compare2face(face['faces'], otherFaces['faces'])
                threshold = 0.90  # set yourself to meet your requirement
                if distance <= threshold:
                    print('-------------------------------')
                    print(otherFaces['filename'])
                    print('-------------------------------')
                    arr.append(otherFaces['filename'])
                    arr.append(face['filename'])
                    clusterList[len(clusterList) - 1].append(otherFaces['filename'])
    else:
        print('already')

print('=================')
print(arr)
print('=================')
print(clusterList)

for idx, list in enumerate(clusterList):
    path = os.getcwd() + "/results/cluster{0}".format(idx)
    os.mkdir(path)
    for element in list:
        shutil.copy(element, path)
