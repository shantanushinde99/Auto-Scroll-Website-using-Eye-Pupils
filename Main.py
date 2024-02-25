from tkinter import *
import sys
import time
import cv2
from gaze_tracking import GazeTracking
from plyer import notification
import mouse
import keyboard
import os
root = Tk()
root.overrideredirect(True)
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
#root.geometry("%dx%d" % (width, height))
root.geometry("40x26")
root.geometry("+%d+%d" % ((width)/2,height*0.1))
root.wm_attributes("-transparentcolor","grey")
root.attributes("-topmost",True)
root.attributes("-alpha",0.2)
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, "Eye.png")
img= PhotoImage(file=image_path)
my_label= Label(root,border=0,bg='grey',image=img)
my_label.pack(fill=BOTH,expand=True)
gaze = GazeTracking()
address = "http://192.168.45.224:8080/video"
webcam = cv2.VideoCapture(address)

def run():

    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    
    
    br = gaze.is_blinking()
    cv2.putText(frame, str(br) , (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    if type(br)==float:
        root.attributes("-alpha",1.0)
        if br > 3.73:                       #Keep changing 3.73 by 0.1 to adjust at scrolling down sensitivity
            mouse.wheel(-2)
        elif br < 3.17:                     #Keep changing 3.17 by 0.1 to adjust at scrolling up sensitivity
            mouse.wheel(2)
    else:
        root.attributes("-alpha",0.1)
    
    #cv2.imshow("Demo", frame)


def animate(e):
    value=0.0
    if e.char=='q':
        notification.notify(title="Gaze AutoScroll",message="starting gaze tracking, press q again to exit")
        #print("starting animation")
        for k in range(20):
            value=value+0.05
            time.sleep(0.1)
            root.attributes('-alpha',value)
        while True:
            run()
            #print("running")
            if keyboard.is_pressed('q'):
                notification.notify(title="Gaze AutoScroll",message="ending gaze tracking")
                #print("ending")
                break
        webcam.release()
        cv2.destroyAllWindows()
        root.quit()
        sys.exit("ended") 

root.bind("<KeyPress>",animate)
#print("start")
notification.notify(title="Gaze AutoScroll",message="click the Eye icon and press q")
root.mainloop()
