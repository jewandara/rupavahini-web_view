#################################################################
######################## Sira Version 2.0.1 #####################
#################################################################
import sys
import os
import re

def SPLIST(CHAR, DESCRIPTION):
     return re.split(CHAR, DESCRIPTION)

def SEARCH(FIRST_STR, LAST_STR, WORD):
     DES_STR = FIRST_STR + '(.*?)' + LAST_STR
     return re.findall((DES_STR), WORD)

def FIND(WORD, DESCRIPTION):
     if (DESCRIPTION.find(WORD) != -1): return 1
     else: return 0

def CHECK_IP(DATA_STRING):
     try:
          IP_ARRY = []
          IP_ARRY_DATA = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str(DATA_STRING))
          if(IP_ARRY_DATA != []):
               for i in range(len(IP_ARRY_DATA)):
                    IP = (IP_ARRY_DATA[i]).strip(" ")
                    if(VALIDATE_IP(IP)):
                         IP_ARRY.append(IP)
          return IP_ARRY
     except: return []

def VALIDATE_IP(ip):
    a = ip.split('.')
    if len(a) != 4: return 0
    for x in a:
        if not x.isdigit(): return 0
        i = int(x)
        if i < 0 or i > 255: return 0
    return 1


