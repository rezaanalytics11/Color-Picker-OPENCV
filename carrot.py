import cv2
import numpy as np
img=cv2.imread(r'C:\Users\Ariya Rayaneh\Desktop\carrot.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#img[np.where((img==[255,255,255]).all(axis=2))]=(0,0,0)

print(img.shape)

mask=np.zeros((256,197,3),dtype='uint8')
mask1=np.ones((256,197,3),dtype='uint8')

R,G,B=cv2.split(mask)

R[65:256,0:197]=0
G[65:256,0:197]=255
B[65:256,0:197]=0

R1,G1,B1=cv2.split(mask)
#
R1[0:65,0:197]=0
G1[0:65,0:197]=255
B1[0:65,0:197]=0

mask1=cv2.merge([R1,G1,B1])


mask=cv2.merge([R,G,B])
result=mask*img

result1=mask1*img
w,h,c=result.shape

result=result1+result
result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
result[np.where((result==[0,0,0]).all())]=(255,255,255)
cv2.imshow('output',result)
cv2.waitKey()