import time, os
import send_message
# import cluster_demo as cluster
# import detection.src.webcam_detect as detect

print("Starting Unsupervised Clustering Package...")
start = time.time()
print("Initiating MTCNN Module")
os.system('python webcam_detect.py')
print("Sleeping for 30 seconds, and clearing GPU memory")
time.sleep(10)
print("Initiating Unsupervised Clustering using Facenet")
# cluster.make_cluster()
os.system("python cluster_demo.py")

send_message.send_message()
end = time.time()
print("Execution Time : " + str((end - start)/60) + " mins, with 30seconds of sleep time")
