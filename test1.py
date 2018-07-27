# a = ["a", "b", "c", "d", "e"]
# for idx, item in enumerate(a[:]):
#     print item
#     if item == "b":
#         a.remove(item)
# print(a)
# x = []
# print(len(x))
import itertools

a = [1,1,2,3,4,4,3,1]
# clusterList = []
# for idx, num in enumerate(a):
#     clusterList.append([])
#     for idx1, otherNum in enumerate(a):
#         if (num == otherNum):
#             clusterList[idx].append(otherNum)

clusterList = list()
clusterList2 = list()
arr = list()
for idx, num in enumerate(a):
    clusterList.append([])
    if not num in arr:
        print(str(a) + "~~~~~~~~~~~")
        for idx1, otherNum in enumerate(a):
            if (num == otherNum):
                arr.append(otherNum)
                clusterList[idx].append(otherNum)
                # a.remove(a[idx1])
            else:
                # clusterList.append([])
                print("printed")
            
    print(str(a) + "Down~~~~")

print(clusterList)
clusterList.sort()

print(list(clusterList for clusterList,_ in itertools.groupby(clusterList)))

# distinctList = list(clusterList for clusterList,_ in itertools.groupby(clusterList))
