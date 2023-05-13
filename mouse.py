import cv2
import mediapipe
import pyautogui

cam = cv2.VideoCapture(0)
faceMesh=mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screenW, screenH=pyautogui.size()

while (cam.isOpened()):
    ret, frame=cam.read()
    frame=cv2.flip(frame,1)
    colorFrame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output=faceMesh.process(colorFrame)
    landMarkPoints=output.multi_face_landmarks
    frameH,frameW,framez=frame.shape
    if (landMarkPoints):
        landMarks=landMarkPoints[0].landmark
        for id, landmark in enumerate(landMarks[474:478]):
            x=int(landmark.x * frameW)
            y=int(landmark.y * frameH)
            cv2.circle(frame,(x,y),3,(0,0,255))
            if id==1:
                screenX=(screenW/frameW)*x
                screenY=(screenH/frameH)*y
                pyautogui.moveTo(screenX,screenY)
            

    #print(landMarkPoints)
    cv2.imshow('eye',frame)




    if (cv2.waitKey(1)==ord('s')):
        break

cam.release()
cv2.destroyAllWindows()

