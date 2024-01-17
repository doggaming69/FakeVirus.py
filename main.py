from plyer import notification #send this to your friends who dont know tech
import time
from tkinter import *
import socket
import os
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
window = Tk() #the windows will gaslight the victim into believing data is being sent
label = Label(window,
    text = "ALL PASSWORDS AND DATA BEING SENT TO SERVERS IN 30 SECONDS CLOSE WINDOW OR SYSTEM WILL BE TERMINATED",
    font = ('arial',15,'bold'),
    foreground = "red",
    background = "black",
    relief=RAISED,
    bd =10,
    padx=20
)
label.pack()
window.mainloop()
window = Tk()
label = Label(window,
    text = "Good choice mutt "+hostname+" "+IPAddr,
    font = ('arial',10,'bold'),
    foreground = "green",
    background = "black",
    relief=RAISED,
    bd =10,
    padx=20
)
label.pack()
window.mainloop()
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10,  # The notification will automatically close after 10 seconds
    )

if __name__ == "__main__":
    notification1_title = "SENDING DATA"
    notification1_message = "30 SECONDS LEFT"

    notification2_title = "completed"
    notification2_message = "ALL DATA SENT TO SERVERS"

    show_notification(notification1_title, notification1_message)
    time.sleep(30)  # Adding a delay between notifications
    show_notification(notification2_title, notification2_message)
