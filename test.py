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

if os.path.exists("results"):
    shutil.rmtree("results")

os.mkdir('results')
def compare2face(img1,img2):
    # face1 = getFace(img1)
    # face2 = getFace(img2)
    if img1 and img2:
        # calculate Euclidean distance
        dist = np.sqrt(np.sum(np.square(np.subtract(img1[0]['embedding'], img2[0]['embedding']))))
        return dist
    return -1

for filename in os.listdir(os.getcwd()+"/images/"):
    # print(str(filename))
    filename1 = os.getcwd()+"/images/"+str(filename)
    if '.jpg' in filename1:
        imageList.append(filename1)

# print(flagList)
for filename in imageList[:]:
    img1 = cv2.imread(filename)
    faces = face_match_demo.getFace(img1)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print(faces)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if len(faces) != 0:
        imageList.remove(filename)
        newImageList.append(filename)
        facesList.append(faces)
    else:
        print("No Faces")


length = [False] * len(newImageList)
flagList = length
writeFlag = [True] * len(newImageList)

# print(len(facesList))
for idx, face in enumerate(facesList[:]):
    # print("Getting Face : " + str(face))
    clusterList.append([])
    if (len(face) != 0):
        for idx1, otherFace in enumerate(facesList[:]):
            if(len(otherFace) != 0):
                # print("------------------------------------------------------------------")
                # print("Comparing : ... \n\nSource :" + imageList[idx] + "\nTarget " + imageList[idx1])
                # if face is otherFace:
                #     print("SAME FILE... Ignoring")
                #     path = os.getcwd() + "/results/cluster{0}".format(idx)
                #     if os.path.exists(path):
                #         # shutil.copy(newImageList[idx], path)
                #         clusterList[idx].append(imageList[idx1])
                #         print("Path exists")
                #         # writeFlag[idx] = True
                #     else:
                #         os.mkdir(path)
                #         # shutil.copy(newImageList[idx], path)
                #         clusterList[idx].append(newImageList[idx1])
                #         print("Path doesnt exists")
                #         # writeFlag[idx] = True

                # else:

                distance = compare2face(face, otherFace)
                threshold = 1.10    # set yourself to meet your requirement
                
                # print("distance = "+str(distance))
                # print("Result = " + (True if distance <= threshold else False))
                if distance <= threshold:
                    flagList[idx1] = True
                    print("Setting Flag at Index "+str(idx1))
                    print(flagList)
                #     dir = str(os.getcwd() + "/dir" + str(idx))
                #     if os.path.exists(dir):
                #         shutil.move(imageList[idx1], dir)
                #     else:
                #         os.mkdir(dir)
                #         shutil.move(imageList[idx1], dir)
                #     print("hello")
                else:
                    print("\nNO MATCH")
            elif (len(otherFace) == 0):
                print("No Faces")
        for idx2, isFace in enumerate(flagList[:]):
            # print("~~~~~~~~~~~~~~~~Inside flagList Itertion~~~~~~~~~~~~~~" + str(writeFlag) + str(idx))
            if(isFace):
                # path = os.getcwd() + "/results/cluster{0}".format(idx)
                # if os.path.exists(path):
                    # shutil.copy(newImageList[idx2], path)
                    clusterList[idx].append(newImageList[idx2])
                    # imageList.remove(idx)
                    # writeFlag[idx2] = False
                # else:
                    # os.mkdir(path)
                    # shutil.copy(newImageList[idx2], path)
                    # clusterList[idx].append(newImageList[idx2])
                    # imageList.remove(idx)
                    # writeFlag[idx2] = False
        del flagList[:]
        flagList = [False] * len(newImageList)
    elif (len(face) == 0):
        print("No Faces")

# for filename in os.listdir(os.getcwd()+"/results/"):
#     # print(filename + "filename is Printed Successfully")
#     filename1 = os.getcwd()+"/results/"+str(filename)
#     if '.jpg' in filename1:
print(clusterList)
clusterList.sort()
print(list(clusterList for clusterList,_ in itertools.groupby(clusterList)))

distinctList = list(clusterList for clusterList,_ in itertools.groupby(clusterList))

for idx, list in enumerate(distinctList):
    path = os.getcwd() + "/results/cluster{0}".format(idx)
    os.mkdir(path)
    for element in list:
        shutil.copy(element, path)

