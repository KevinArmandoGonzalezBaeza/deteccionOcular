import cv2
import mediapipe
import pyautogui
import time

#473 es el punto de iris

cam = cv2.VideoCapture(0)
faceMesh=mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screenW, screenH=pyautogui.size()
wingNum=0

while (cam.isOpened()):
    ret, frame=cam.read()
    frame=cv2.flip(frame,1)
    colorFrame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output=faceMesh.process(colorFrame)
    landMarkPoints=output.multi_face_landmarks
    frameH,frameW,framez=frame.shape
    if (landMarkPoints):
        landMarks=landMarkPoints[0].landmark
        for id, landmark in enumerate(landMarks[473:478]):
            irisx=int(landMarks[473].x*frameW)
            irisy=int(landMarks[473].y*frameH)
            cv2.circle(frame, (irisx,irisy),3,(0,0,255))
            if id == 1:
               screenX=screenW*landMarks[473].x
               screenY=screenH*landMarks[473].y
               pyautogui.moveTo(screenX,screenY)

        #se define un arreglo con las coordenadas del ojo derecho
        right=[landMarks[374], landMarks[386]]
        for landmark in right:
            x=int(landmark.x*frameW)
            y=int(landmark.y*frameH)
            cv2.circle(frame, (x,y),3,(0,0,255))
        if (right[0].y-right[1].y)< 0.002 and (left[0].y-left[1].y)>0.002:
            pyautogui.click(button="right")
            pyautogui.sleep(1)

        #se define un arreglo con las coordenadas del ojo izquierdo
        left=[landMarks[145], landMarks[159]]
        for landmark in left:
            x=int(landmark.x*frameW)
            y=int(landmark.y*frameH)
            cv2.circle(frame, (x,y),3,(0,255,255))
            
        if (left[0].y-left[1].y) < 0.002 and (right[0].y-right[1].y)>0.002:
            pyautogui.click()
            pyautogui.sleep(1)
            
    cv2.imshow('eye',frame)




    if (cv2.waitKey(1)==ord('s')):
        break

cam.release()
cv2.destroyAllWindows()

