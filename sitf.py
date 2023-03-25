import cv2
import numpy as np

#se carga la imagen en la que se van a buscar las caracteriscas
img=cv2.imread("img.png",cv2.IMREAD_GRAYSCALE)

#se crea una instancia de la libreria de SIFT para poder trabajar con ella
sift=cv2.xfeatures2d.SIFT_create()


#surft=cv2.xfeatures2d.SURF_create()
orb=cv2.ORB_create()

#keypoints, descriptors=sift.detectAndCompute(img, None)
#keypoints, descriptors=surft.detectAndCompute(img, None)
keypoints, descriptors=orb.detectAndCompute(img, None)

img=cv2.drawKeypoints(img,keypoints,None)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

