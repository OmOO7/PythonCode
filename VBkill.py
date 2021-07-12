# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 12:50:10 2021

@author: Arjun
"""

import sched, time
import psutil
import os
tmp_ProcessId = None
tmp_ProcessName = None
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


def MatchId(tmp_Id,orig_Id,tmp_Name,orig_Name):
    if ((tmp_Id == orig_Id) and (tmp_Name == orig_Name)) :
            print('ProcessId Match')
            os.kill(tmp_Id,9)
    else :
            print('ProcessId not Match')
def do_something(sc): 
    global tmp_ProcessId
    global tmp_ProcessName
    processID = None
    processName = None
    listOfProcessIds = findProcessIdByName('wscript')
    if len(listOfProcessIds) > 0:
        print('Process Exists | PID and other details are')
        for elem in listOfProcessIds:
            processID = elem['pid']
            processName = elem['name']
            processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
            print((processID ,processName,processCreationTime ))
            s.enter(10, 1, do_something, (sc,))
            MatchId(tmp_ProcessId,processID,tmp_ProcessName,processName)
            tmp_ProcessId = processID
            tmp_ProcessName = processName                    
            #print(tmp_ProcessId)
                            
    else :
        print('No Running Process found with given text')
        # do your stuff
        s.enter(10, 1, do_something, (sc,))
        

s.enter(10, 1, do_something, (s,))
s.run()