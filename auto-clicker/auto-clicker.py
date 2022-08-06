import time as wait
try:
  import pyautogui as pag
except:
	print("please go to pypi.org to download pyautogui, this project need that.")
	wait.sleep(1)
	raise("")
keydict = {0:"left",1:"right",2:"middle"}
while True:
    times = int(input("please input click times"))
    time = float(input("please input interval time(second)"))
    key = keydict[int(input("please input button(left input 0,right input 1,middle input 2)"))]
    for i in range(5):
        wait.sleep(1)
        print(5 - i)
    pag.click(clicks=times,interval=time,button=key)
