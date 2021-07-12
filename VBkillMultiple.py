# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 15:17:34 2021

@author: Arjun
"""


import sched, time
import psutil
import os
import numpy as np
tmp_ProcessId = []
tmp_ProcessName = []
AppendCounter = 0

s = sched.scheduler(time.time, time.sleep)
def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
    
    listOfProcessObjects = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcessObjects;

# def ResetCounter():
#     global AppendCounter
#     AppendCounter = 0
    
def MatchId(tmp_Id,orig_Id,tmp_Name,orig_Name):
    global AppendCounter
    global tmp_ProcessId
    global tmp_ProcessName
    #print("temp Id lenght ",len(tmp_Id))
    #print(tmp_Id)
    #print(orig_Id)
    if(np.array_equal(tmp_Id,orig_Id)):
        print('ProcessId Match')
        for x in tmp_Id :
            os.kill(x,9) 
        tmp_ProcessId = []
        tmp_ProcessName = []
        AppendCounter = 9
    else:
        print('Process not Match')
    #for x in range(len(tmp_Id)):
    #if ((tmp_Id == orig_Id) and (tmp_Name == orig_Name)) :
    #    print('ProcessId Match')
    #    os.kill(tmp_Id,9)       
    #else :
     #   print('ProcessId not Match')
        
    
def GetProcess(sc): 
    global tmp_ProcessId
    global tmp_ProcessName
    global AppendCounter
    processID = []
    processName = []
    listOfProcessIds = findProcessIdByName('wscript')
    if len(listOfProcessIds) > 0:
        print('Process Exists | PID and other details are')
        #print("Append Counter Value--------", AppendCounter)
        if(AppendCounter == 10):
                AppendCounter = 0
                
        for elem in listOfProcessIds:
            #processID = elem['pid']
            #processName = elem['name']
            processID.append(elem['pid'])
            processName.append(elem['name']) 
            processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
            print((processID ,processName,processCreationTime ))
            s.enter(10, 1, GetProcess, (sc,))
            #if (AppendCounter == 3) :
            MatchId(tmp_ProcessId,processID,tmp_ProcessName,processName)
            if (AppendCounter <= 1) :   
                tmp_ProcessId.append(elem['pid'])
                print("Appending process ID",tmp_ProcessId)
                tmp_ProcessName.append(elem['name'])
            
            print("Append Counter Value", AppendCounter)
            AppendCounter +=1
            
        #print("Original Process id",len(processID))
        
         
                            
    else :
        print('No Running Process found with given text')
        # do your stuff
        s.enter(10, 1, GetProcess, (sc,))
        

s.enter(10, 1, GetProcess, (s,))
s.run()