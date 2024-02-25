from tkinter import *
import time
import example as ex
from PIL import ImageTk, Image
root = Tk()
root.overrideredirect(True)
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
#root.geometry("%dx%d" % (width, height))
root.geometry("40x26")
root.geometry("+%d+%d" % ((width)/2,height*0.1))

root.wm_attributes("-transparentcolor","grey")
root.attributes("-topmost",True)
root.attributes("-alpha",0.0)
global state 
state=True
def animate(e):
    running=state
    value=0.0
    if e.char=='q' and running==False:
        state=True
        for k in range(20):
            value=value+0.05
            time.sleep(0.1)
            root.attributes('-alpha',value)
        ex.run()
    
    elif e.char=='w':
        state=False
        root.quit()
img= PhotoImage(file="R.png")
my_label= Label(root,border=0,bg='grey',image=img)
root.bind("<KeyPress>",animate)
my_label.pack(fill=BOTH,expand=True)
root.mainloop()
animate()


