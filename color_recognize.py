import cv2

image=cv2.imread(r'C:\Users\Ariya Rayaneh\Desktop\result\logo1_changeValue1.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(image.shape)
print(image)



def red_recognize(img):
  k=0
  R,G,B = cv2.split(img)
  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for c in range(img.shape[2]):
            if R[i:i+1 , j:j+1]==250 and G[i:i+1 , j:j+1]==0 and B[i:i+1 , j:j+1]==1:
                k=k+1

  print('{} pixels are red!'.format(k))

def draw(img):

 img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 cv2.imshow('output',img)
 cv2.waitKey()

red_recognize(image)

draw(image)



