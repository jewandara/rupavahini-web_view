import time
import sys
import os
import threading
import logging
import datetime


#################################################################################################################################

def Display(DATA):
     sys.stdout.write('| RECEIVER '+str(DATA)+'\n')
     sys.stdout.flush()


def Main():
     while True:
          Display('( [*] Main->Testing ) : MAIN FUNCTION TESTING IN A THREAD')
          time.sleep(0.7)



#################################################################################################################################
if __name__ == '__main__':
     MainThread = threading.Thread(target=Main())
     MainThread.start()
