import os
import cv2
import numpy as np
import shutil
import itertools

import face_match_demo


imageList = list()
facesList = list()
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

for filename in os.listdir(os.getcwd()+"/images/"):
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
        facesList.append(faces)
    else:
        print("No Faces")


length = [False] * len(newImageList)
flagList = length
writeFlag = [True] * len(newImageList)

# print(len(facesList))
for idx, face in enumerate(facesList[:]):
    if not imageList[idx] in arr:
        print(imageList[idx])
        clusterList.append([])
        for idx1, otherFace in enumerate(facesList[:]):
            # if(len(otherFace) != 0):
            distance = compare2face(face, otherFace)
            threshold = 0.96  # set yourself to meet your requirement
            if distance <= threshold:
                arr.append(newImageList[idx])
                arr.append(newImageList[idx1])
                clusterList[len(clusterList) -1].append(newImageList[idx1])
            # else:
            #     print("\nNO MATCH")
        # print(clusterList)
    else:
        print("already used")
        # elif (len(otherFace) == 0):
        #     print("No Faces")
        # for idx2, isFace in enumerate(flagList[:]):
        #     if(isFace):
        #         clusterList[idx].append(newImageList[idx2])          
        # del flagList[:]
        # flagList = [False] * len(newImageList)
    # elif (len(face) == 0):
        # print("No Faces")

# for x in facesList:
#     print(x[0])
# print(clusterList)
clusterList.sort()
# print(list(clusterList for clusterList,_ in itertools.groupby(clusterList)))

distinctList = list(clusterList for clusterList,_ in itertools.groupby(clusterList))

for idx, list in enumerate(distinctList):
    path = os.getcwd() + "/results/cluster{0}".format(idx)
    os.mkdir(path)
    for element in list:
        shutil.copy(element, path)

