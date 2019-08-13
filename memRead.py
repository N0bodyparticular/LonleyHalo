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

ADDRESS = 0x400008CC
import time

buffer = ctypes.c_char_p("Hello, world".encode('utf-8'))
bufferSize = 8#len(buffer.value)
bytesRead = ctypes.c_ulong(0)


while 1:    
    memory_value = ReadProcessMemory(processHandle, ADDRESS, buffer, bufferSize, ctypes.byref(bytesRead)) # Why is it one?
    print("Health: " + str(buffer.value))
    
    time.sleep(0.5)
