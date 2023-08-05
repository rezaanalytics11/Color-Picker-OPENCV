import cv2
import numpy as np
# img=cv2.imread(r'C:\Users\Ariya Rayaneh\Desktop\obama.jpg')
# image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(img.shape)
#
# R,G,B=cv2.split(img)
#
#
# aa=cv2.merge([B,R,G])
#
#
# cv2.imshow('output',aa)
# cv2.waitKey()

logo=np.ones((500,1000,3),dtype='uint8')*80
logo = cv2.cvtColor(logo, cv2.COLOR_BGR2RGB)
R,G,B=cv2.split(logo)

R[100:200,100:200]=20
G[100:200,100:200]=83
B[100:200,100:200]=246

R[210:310,210:310]=0
G[210:310,210:310]=185
B[210:310,210:310]=255
#
R[210:310,100:200]=239
G[210:310,100:200]=164
B[210:310,100:200]=0
#
R[100:200,210:310]=0
G[100:200,210:310]=186
B[100:200,210:310]=127



result=cv2.merge([R,G,B])

print(result.shape)

cv2.putText(result,"Microsoft",(370,250),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),12)
k=[]
for i in range(result.shape[0]):
    for j in range(result.shape[1]):
            k.append(result[i,j])

if k[0][0]==80 & k[0][1]==80:
  print('yes')
# for i in k:
#     if i==np.array([80,80,80]):
#         print('hello')
cv2.imshow('output',result)
cv2.imwrite('C:\Users\Ariya Rayaneh\Desktop\microsoft.jpg',result)
cv2.waitKey()