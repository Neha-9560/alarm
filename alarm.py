import datetime
import time
#from playsound import playsound
import winsound
alarmhour=int(input("Enter Hour: "))
alarmmin=int(input("Enter Minute: "))
alarmam=input("Enter AM/PM: ")
if alarmam=="PM" and alarmam!=12:
    alarmhour+=12
elif alarmam=="AM" and alarmam==12:
    alarmhour=0

while True:    
    if alarmhour==datetime.datetime.now().hour and alarmmin==datetime.datetime.now().minute:
       print("Playing..")
       for _ in range(5):
          winsound.PlaySound(r"C:\Users\dell\Desktop\python\Projectss\alarm.wav", winsound.SND_FILENAME)
       break 
    time.sleep(1)