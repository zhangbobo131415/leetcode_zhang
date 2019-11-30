# encoding: UTF-8
import glob as gb
import cv2
import os
import numpy as np


img_path = gb.glob(r"F:\random_rota*.jpg")

videoWriter = cv2.VideoWriter('D:\\add\\testTTT.mp4', cv2.VideoWriter_fourcc(*'XVID'), 60, (1440,960))  #cv2.VideoWriter_fourcc(*'MJPG')

reader1 = cv2.VideoCapture("D:\\add\\Oigin_SDBronze.mp4")
reader2 = cv2.VideoCapture("D:\\add\\record.avi")
framenum = 1
while 1:
    if framenum%2==1:
        ret,img1 = reader1.read()
    ret,img2 = reader2.read()
    img3 = np.zeros((960,1440,3), np.uint8)
    if framenum<1436:
        img3[240:720,0:1440] = np.concatenate((img1,img2),axis=1)  #(1440,480)

    else:
        img3[0:960,360:1080] = np.concatenate((img1,img2),axis=0)  #(720,960)
    #img3=cv2.resize(img3,(1440,760),interpolation=cv2.INTER_CUBIC)

    videoWriter.write(img3)
    framenum = framenum + 1

print(framenum)


'''
reader = cv2.VideoCapture("D:\\testPic\\MVBronze\\Oigin_SDBronze.mp4")
framenum = 2
ret,img2 = reader.read()    #read first
ret,img2 = reader.read()    #read second   
for path in img_path:
    img  = cv2.imread(path) 
    print path
    #img = cv2.resize(img,(720,480))
    
    if framenum%2==1:
    	ret,img2 = reader.read()
    img3=np.concatenate((img,img2),axis=1)
	#cv2.imwrite("D://testPic//MVBronze//img3//"+str(framenum)+".bmp",img3)
    framenum = framenum + 1

    #cv2.imshow('im3',img3)
    videoWriter.write(img3)
'''
'''
for x in range(len(img_path)):
    path1 = img_path[x]
    if x%2==0:
        path2 = img_path[x+1]
    else:
        paht2 = path1
    print path1,path2
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    img3=np.concatenate((img1,img2),axis=1)
    img3=cv2.resize(img3,(1440,760),interpolation=cv2.INTER_CUBIC)
    videoWriter.write(img3)
'''





'''
imgpath = 'D:\\testPic\\MVBronze\\'
dirs = os.listdir(imgpath)
dirs.sort(reverse = False)
for img in dirs:
	if os.path.splitext(img)[1] == '.bmp':
		print img
'''
'''
img1 = cv2.imread('D://testPic//5.jpg')
img2 = cv2.imread('D://testPic//6.jpg')
img3 = np.zeros((img1.shape[0],img1.shape[1]*2),np.uint8)

#print img1[:,[0,100],0]
#img3 = img1+img2
#
#for ch in range(0,3):
#	img3[:,:,ch]
#	
#img3[:,[0,img1.shape[1]],:] = img1[:,:,:]
#img3[[0,100],:,1] = img1[[0,100],:,1]
img3=np.concatenate((img1,img2),axis=1)
cv2.imshow('3',img3)
cv2.waitKey(0)
'''