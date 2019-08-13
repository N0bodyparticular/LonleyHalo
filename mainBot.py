import keyboard, time, random, threading

hellishness = 5 # this is 1-10 scale.
# you neeed to bind shoot to v.




import win32gui,win32com.client
import win32api
import ctypes
import win32ui
import win32process 
from ctypes import wintypes

### Initializing functions and permissions ###
OpenProcess = ctypes.windll.kernel32.OpenProcess
ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory # Method 1

PROCESS_ALL_ACCESS = 0x1F0FFF
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_OPERATION = 0x0008
PROCESS_VM_READ = 0x0010
PROCESS_VM_WRITE = 0x0020
### End of Initializing session

### Getting process handle ###
HWND = win32ui.FindWindow(None,'Halo').GetSafeHwnd()
PID = win32process.GetWindowThreadProcessId(HWND)[1]
processHandle = OpenProcess(PROCESS_ALL_ACCESS, False, PID) 
### End of Getting process handle ###

### Reading value of a Memory Address ###

ADDRESS = 0x400008CC # adress of crosshair color



buffer = ctypes.c_char_p("Hello, world".encode('utf-8'))
bufferSize = 8#len(buffer.value)
bytesRead = ctypes.c_ulong(0)




#

doBot = False
runBot = False

def updateBot(): # update the doBot status depending on user input
    global doBot
    lastbot = False
    
    while 1:
        bt = keyboard.is_pressed('caps lock')
        if bt == False and lastbot == True:
            # we have a toggle
            doBot = not doBot

            if doBot:
                keyboard.press('shift')
            else:
                keyboard.release('shift')
                releaseAll()
                
            print(doBot)

        lastbot = bt
        
        time.sleep(0.01)
        
threading.Thread(target=updateBot).start()

def updateFire():
    global controls

    cooldown = 0

    while 1:
        time.sleep(0.1)
        if doBot:
            if controls[3] == 1:
                # we want to fire.
                if cooldown <= 0:
                    memory_value = ReadProcessMemory(processHandle, ADDRESS, buffer, bufferSize, ctypes.byref(bytesRead)) # Why is it one?
                    print(buffer.value)
                    if buffer.value:
                        
    
    
                        keyboard.press('v')
                        time.sleep(0.1)
                        keyboard.release('v')
                        cooldown  = 11-hellishness
                cooldown  = cooldown - 1
                


threading.Thread(target=updateFire).start()



def updateMove():
    global controls


    while 1:
        time.sleep(0.1)
        if doBot:
            releaseAll()
            if controls[0] == -1: keyboard.press('a')
            if controls[0] == 1: keyboard.press('d')
            if controls[1] == -1: keyboard.press('s')
            if controls[1] == 1: keyboard.press('w')
            if controls[2] == -1: keyboard.press('control')
            if controls[2] == 1: keyboard.press('space')
            
threading.Thread(target=updateMove).start()            
            


def updateLoadout():
    while 1:
        time.sleep(0.35)
        if doBot:
            action = random.randint(0,125)
            if action == 1: #reload current weapon
                keyboard.press('r')
                time.sleep(0.05)
                keyboard.release('r')
                print("Reloading...")
            elif action == 2: # do pocket reload glitch
                keyboard.press('r')
                time.sleep(0.05)
                keyboard.release('r')
                time.sleep(0.05)
                keyboard.press('r')
                time.sleep(0.05)
                keyboard.release('r')
                time.sleep(0.05)
                keyboard.press('tab')
                time.sleep(0.1)
                keyboard.release('tab') # hehe very sneaky
                print("Reloading both weapons...")
            elif action == 3: # switch weapon
                keyboard.press('tab')
                time.sleep(0.1)
                keyboard.release('tab')
                print("Switching weapons")
                
            else:
                pass
threading.Thread(target=updateLoadout).start() 

                
                
            
            








def releaseAll():
    keyboard.release('w')
    keyboard.release('a')
    keyboard.release('s')
    keyboard.release('d')
    #keyboard.release('shift')
    keyboard.release('control')
    keyboard.release('r')
    keyboard.release('space')
    #keyboard.release('v')
    # the commented ot keys are controlled seperatl*e*y





firecool = 0

moveCool = 0
    


controls = [0,0,0,0]
# right, forwards, crouch/jump, fire
while 1:
    
    time.sleep(0.1)
    if doBot:
        # run the bot program.
        # we set the control vector accordingly.
        moveCool = moveCool+1

        if random.randint(0, 4) == 1:
            controls[0] = random.choice([-1,0,1])

        if random.randint(0, 5) == 1:
            controls[1] = random.choice([-1,0,1,1,1])

        if random.randint(0, 10) == 1:
            controls[2] = random.choice([-1,-1,0,0,0,0,0,1])

        if random.randint(0, 10) == 1:
            controls[3] = random.choice([1])
        print(controls)
        

        
            
            
