
from tkinter import *
import os


root = Tk()
root.title("Shutdown App")
root.geometry("420x420")

def restart():
    os.system("shutdown /r /t 10")

def shutdown():
    os.system("shutdown /s /t 1")

def logout():
    os.system("shutdown -l")

#First Button - restart
restart_button = PhotoImage(file = "restartButton.png")
first_button = Button(root,image = restart_button,borderwidth = 0, cursor = "hand2", command = restart)
first_button.place(x=10,y=10)

#Second Button - shutdown
shutdown_button = PhotoImage(file = "shutdownButton.png")
second_button = Button(root,image = shutdown_button,borderwidth = 0, cursor = "hand2", command = shutdown )
second_button.place(x=200,y=10)

#Third Button - logout
logout_button = PhotoImage(file = "logoutButton.png")
third_button = Button(root, image = logout_button, borderwidth = 0, cursor = "hand2", command = logout)
third_button.place(x=200,y=200)

root.mainloop()