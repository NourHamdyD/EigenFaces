import cv2
import os
# resize all images of a directory to a given size
count = 1
def resize(dir, size):
    global count
    for file in os.listdir(dir):
        if file.endswith(".jpg"):
            img = cv2.imread(dir + file)
            img = cv2.resize(img, size)
            cv2.imwrite(dir + file, img)
            print("Resized " + str(count) + " images")
            count += 1
            

resize("fish/", (92, 112))