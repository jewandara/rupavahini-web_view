##################################
##      SUB INTERFACE - 1       ##
##      MGT INTERFACE - 2       ##
##      COM INTERFACE - 3       ##
##################################
import re
import server

def split_string(description):
    return re.split(':', description)

def VALIDATE_IP(ip):
    a = ip.split('.')
    if len(a) != 4: return 0
    for x in a:
        if not x.isdigit(): return 0
        i = int(x)
        if i < 0 or i > 255: return 0
    return 1

def FIND_IP(DES_STR):
    try:
        IP = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str(DES_STR) )
        count = len(IP)
        for i in range(0, count):
            if (VALIDATE_IP(IP[i])>0): return IP[i]
    except ValueError: return 0
    except IndexError: return 0

def VALIDATE_SUB(DES_ARRY, INDEX, COUNT):
    try:
        SUB_NUM = str(DES_ARRY)[INDEX:(INDEX+COUNT)]
        SUB = int(SUB_NUM)
        if(len(str(SUB))==COUNT): return SUB
        else: return 0
    except ValueError: return 0
    except IndexError: return 0

def FIND_SUB(DES_ARRY):
    try:
        index_1 = str(DES_ARRY).find("99")
        index_2 = str(DES_ARRY).find("97")
        index_3 = str(DES_ARRY).find("7000")
        index_4 = str(DES_ARRY).find("5000")
        SUB_NUM = 0
        if (index_1>-1) and (VALIDATE_SUB(DES_ARRY, index_1, 9)>0) :
            return VALIDATE_SUB(DES_ARRY, index_1, 9)
        elif (index_2>-1) and (VALIDATE_SUB(DES_ARRY, index_2, 9)>0) :
            return VALIDATE_SUB(DES_ARRY, index_2, 9)
        elif (index_3>-1) and (VALIDATE_SUB(DES_ARRY, index_3, 8)>0) :
            return VALIDATE_SUB(DES_ARRY, index_3, 8)
        elif (index_4>-1) and (VALIDATE_SUB(DES_ARRY, index_4, 8)>0) :
            return VALIDATE_SUB(DES_ARRY, index_4, 8)
        else: return 0
    except ValueError: return 0
    except IndexError: return 0

def FIND_MGT(DES_ARRY):
    try:
        DATA = (str(DES_ARRY)).upper()
        if ( (DATA.find("MGT")>-1) or (DATA.find("MGMT")>-1) ): return 1
        else: return 0
    except ValueError: return 0
    except IndexError: return 0

def FIND_SYS(DES_ARRY):
    try:
        DATA = (str(DES_ARRY)).upper()
        if (DATA.find("SYNAPSYS")>-1): return 0
        if (DATA.find("SYSTEM")>-1): return 1
        if (DATA.find("SYS")>-1): return 1
        else: return 0
    except ValueError: return 0
    except IndexError: return 0

def FIND_COMMON(DES_ARRY):
    try:
        DATA = (str(DES_ARRY)).upper()
        if (DATA.find("COMMON")>-1): return 1
        else: return 0
    except ValueError: return 0
    except IndexError: return 0

def FIND_ACCESS(DES_ARRY):
    try:
        DATA = (str(DES_ARRY)).upper()
        if (DATA.find("CAMBIUM")>-1):
            return "CAMBIUM"
        elif (DATA.find("WIBAS")>-1):
            return "WIBAS"
        elif (DATA.find("FIBER")>-1):
            return "FIBER"
        elif (DATA.find("GPON")>-1):
            return "GPON"
        elif (DATA.find("UTP")>-1):
            return "UTP"
        elif (DATA.find("FIB")>-1):
            return "FIBER"
        elif (DATA.find("WIMAX")>-1):
            return "WIMAX"
        elif (DATA.find("CAM")>-1):
            return "CAMBIUM"
        elif (DATA.find("WIB")>-1):
            return "WIBAS"
        elif (DATA.find("OPT")>-1):
            return "FIBER"
        else: return ""
    except ValueError: return ""
    except IndexError: return ""

def FIND_DIRECTION(DES_ARRY):
    try:
        DATA = (str(DES_ARRY)).upper()
        if (DATA.find("P2P")>-1):
            return "P2P"
        elif (DATA.find("P2MP")>-1):
            return "P2MP"
        elif (DATA.find("MP2MP")>-1):
            return "MP2MP"
        elif (DATA.find("PTMP")>-1):
            return "P2MP"
        elif (DATA.find("PTP")>-1):
            return "P2P"
        elif (DATA.find("PTMPT")>-1):
            return "P2MP"
        elif (DATA.find("MPTMP")>-1):
            return "MP2MP"
        else: return ""
    except ValueError: return ""
    except IndexError: return ""

def GET_CX_INDEX(DES_STR):
    try:
        DATA = (str(DES_STR)).upper()
        if (DATA.find("LTD")>-1):
            return 1
        elif (DATA.find("BANK")>-1):
            return 1
        elif (DATA.find("HOSPITAL")>-1):
            return 1
        elif (DATA.find("PLC")>-1):
            return 1
        elif (DATA.find("UNITED")>-1):
            return 1
        elif (DATA.find("PVT")>-1):
            return 1
        elif (DATA.find("LANKA")>-1):
            return 1
        elif (DATA.find("NTB")>-1):
            return 1
        elif (DATA.find("BOC")>-1):
            return 1
        elif (DATA.find("TATA")>-1):
            return 1
        else:
            return 0
    except ValueError: return 0
    except IndexError: return 0

def FIND_CUSTOMER(DES_ARRY):
    count = len(DES_ARRY)
    for i in range(0, count):
        if(GET_CX_INDEX(DES_ARRY[i])>0):
            return DES_ARRY[i]

##################################      
def SUB_INTERFACE(DIRECTION, ACCESS, SUB, CX, IP, DT, DES_ARRY):
    try:
        SQL_ARRY = []
        if(SUB>0):
            if (len(DES_ARRY) == 7):
                CORRECT_SUB = FIND_SUB(DES_ARRY[0])
                if(CORRECT_SUB>0):
                    CORRECT_ACCESS = FIND_ACCESS(DES_ARRY[1])
                    if( CORRECT_ACCESS != "" ):
                        CORRECT_IP = FIND_IP(str(DES_ARRY[2]))
                        if(CORRECT_IP == None): SQL_ARRY = [1, "SUB_INTERFACE", "NONE", 0, "IP IS NOT STANDARD", DT[0], DT[1], DT[2], DT[3], CORRECT_SUB, DIRECTION, CORRECT_ACCESS, DES_ARRY[5], DES_ARRY[6], IP, DES_ARRY[3] ]
                        else: SQL_ARRY = [1, "SUB_INTERFACE", "NONE", 1, "STANDARD", DT[0], DT[1], DT[2], DT[3], CORRECT_SUB, DIRECTION, CORRECT_ACCESS, DES_ARRY[5], DES_ARRY[6], CORRECT_IP, DES_ARRY[3] ]
                        #print(SQL_ARRY)
                    else:
                        SQL_ARRY = [1, "SUB_INTERFACE", "NONE", 0, "ACCESS TYPE IS NOT STANDARD", DT[0], DT[1], DT[2], DT[3], CORRECT_SUB, DIRECTION, ACCESS, DES_ARRY[1], DES_ARRY[2], IP, ""]
                        #print(SQL_ARRY)  
                else:
                    SQL_ARRY = [1, "SUB_INTERFACE", "NONE", 0, "SUB NUMBER IS NOT STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, DES_ARRY[1], DES_ARRY[2], IP, "" ]
                    #print(SQL_ARRY)
            else:
                SQL_ARRY = [1, "SUB_INTERFACE", "NONE", 0, "STANDARD NOT FOUND", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, "" ]
                #print(SQL_ARRY)
            return server.update(SQL_ARRY)
        else:
            return 0
    except ValueError: return 0
    except IndexError: return 0

################################## 
def MGT_INTERFACE(DIRECTION, ACCESS, SUB, CX, IP, DT, DES_ARRY):
    try:
        SQL_ARRY = []
        if (FIND_MGT(DES_ARRY)>0):
            if (len(DES_ARRY) == 8):
                if ((DES_ARRY[0]=='SYS') and (DES_ARRY[1]=='MGT')):
                    CORRECT_ACCESS = FIND_ACCESS(DES_ARRY[2])
                    if ( CORRECT_ACCESS != "" ):
                        CORRECT_DIRECTION = FIND_DIRECTION(DES_ARRY[3])
                        if( CORRECT_DIRECTION != "" ):
                            CORRECT_IP = FIND_IP(str(DES_ARRY[4]))
                            if(CORRECT_IP == None): SQL_ARRY = [3, "MGT_INTERFACE", "CX_LOCATION", 0, "IP IS NOT STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, CORRECT_DIRECTION, CORRECT_ACCESS, DES_ARRY[6], DES_ARRY[7], IP, DES_ARRY[5]]
                            else: SQL_ARRY = [3, "MGT_INTERFACE", "CX_LOCATION", 1, "STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, CORRECT_DIRECTION, CORRECT_ACCESS, DES_ARRY[6], DES_ARRY[7], CORRECT_IP, DES_ARRY[5]]
                            #print(SQL_ARRY)
                        else:
                            CORRECT_IP = FIND_IP(str(DES_ARRY[4]))
                            if(CORRECT_IP == None): SQL_ARRY = [3, "MGT_INTERFACE", "CX_LOCATION", 0, "IP IS NOT STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, CORRECT_ACCESS, DES_ARRY[6], DES_ARRY[7], IP, DES_ARRY[5]]
                            else: SQL_ARRY = [3, "MGT_INTERFACE", "CX_LOCATION", 1, "STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, CORRECT_ACCESS, DES_ARRY[6], DES_ARRY[7], CORRECT_IP, DES_ARRY[5]]
                            #print(SQL_ARRY)
                    else:
                        CORRECT_IP = FIND_IP(str(DES_ARRY[4]))
                        if(CORRECT_IP == None): SQL_ARRY = [3, "MGT_INTERFACE", "CX_LOCATION", 0, "IP IS NOT STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, DES_ARRY[6], DES_ARRY[7], IP, DES_ARRY[5]]
                        else: SQL_ARRY = [3, "MGT_INTERFACE", "CX_LOCATION", 1, "STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, DES_ARRY[6], DES_ARRY[7], CORRECT_IP, DES_ARRY[5]]
                        #print(SQL_ARRY)
                    return server.update(SQL_ARRY)
                elif (FIND_SYS(DES_ARRY)>0):
                    SQL_ARRY = [2, "MGT_INTERFACE", "NONE", 0, "MGT STANDARD NOT FOUND", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, "" ]
                    #print(SQL_ARRY)
                    return server.update(SQL_ARRY)
                else: return 0
            elif (len(DES_ARRY) == 7):
                if ((DES_ARRY[0]=='SYS') and (DES_ARRY[1]=='MGT')):
                    CORRECT_ACCESS = FIND_ACCESS(DES_ARRY[2])
                    if ( CORRECT_ACCESS != "" ):
                        CORRECT_DIRECTION = FIND_DIRECTION(DES_ARRY[3])
                        if( CORRECT_DIRECTION != "" ):
                            CORRECT_IP = FIND_IP(str(DES_ARRY[4]))
                            if(CORRECT_IP == None): SQL_ARRY = [4, "MGT_INTERFACE", "BASE_STATION", 0, "IP IS NOT STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, CORRECT_DIRECTION, CORRECT_ACCESS, CX, "", IP, DES_ARRY[5]]
                            else: SQL_ARRY = [4, "MGT_INTERFACE", "BASE_STATION", 1, "STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, CORRECT_DIRECTION, CORRECT_ACCESS, CX, "", CORRECT_IP, DES_ARRY[5]]
                            #print(SQL_ARRY)
                        else:
                            CORRECT_IP = FIND_IP(str(DES_ARRY[4]))
                            if(CORRECT_IP == None): SQL_ARRY = [4, "MGT_INTERFACE", "BASE_STATION", 0, "IP IS NOT STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, CORRECT_ACCESS, CX, "", IP, DES_ARRY[5]]
                            else: SQL_ARRY = [4, "MGT_INTERFACE", "BASE_STATION", 1, "STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, CORRECT_ACCESS, CX, "", CORRECT_IP, DES_ARRY[5]]
                            #print(SQL_ARRY)
                    else:
                        CORRECT_IP = FIND_IP(str(DES_ARRY[4]))
                        if(CORRECT_IP == None): SQL_ARRY = [4, "MGT_INTERFACE", "BASE_STATION", 0, "IP IS NOT STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, DES_ARRY[5]]
                        else: SQL_ARRY = [4, "MGT_INTERFACE", "BASE_STATION", 1, "STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", CORRECT_IP, DES_ARRY[5]]
                        #print(SQL_ARRY)
                    return server.update(SQL_ARRY)
                elif (FIND_SYS(DES_ARRY)>0):
                    SQL_ARRY = [2, "MGT_INTERFACE", "NONE", 0, "MGT STANDARD NOT FOUND", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, "" ]
                    #print(SQL_ARRY)
                    return server.update(SQL_ARRY)
                else: return 0
            elif (len(DES_ARRY) == 5):
                if ((DES_ARRY[0]=='SYS') and (DES_ARRY[1]=='MGT')):
                    SQL_ARRY = [5, "MGT_INTERFACE", "CX LOCATION DEVICE", 1, "STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, DES_ARRY[3], DES_ARRY[4], IP, "" ]
                    #print(SQL_ARRY)
                    return server.update(SQL_ARRY)
                elif (FIND_SYS(DES_ARRY)>0):
                    SQL_ARRY = [2, "MGT_INTERFACE", "NONE", 0, "MGT STANDARD NOT FOUND", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, "" ]
                    #print(SQL_ARRY)
                    return server.update(SQL_ARRY)
                else: return 0
            else:
                if (FIND_SYS(DES_ARRY)>0):
                    SQL_ARRY = [2, "MGT_INTERFACE", "NONE", 0, "MGT STANDARD NOT FOUND", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, "" ]
                    #print(SQL_ARRY)
                    return server.update(SQL_ARRY)
                else: return 0
        else:return 0
        return 0
    except ValueError: return 0
    except IndexError: return 0

################################## 
def COM_INTERFACE(DIRECTION, ACCESS, SUB, CX, IP, DT, DES_ARRY):
    try:
        SQL_ARRY = []
        if (FIND_SYS(DES_ARRY)>0):
            if (len(DES_ARRY) == 5):
                if (DES_ARRY[0]=='R'):
                    if (DES_ARRY[1]=='SYS'):
                        CORRECT_SUB = FIND_SUB(DES_ARRY[4])
                        if(CORRECT_SUB>0):
                            SQL_ARRY = [7, "COM_INTERFACE", "BACKUP", 1, "STANDARD", DT[0], DT[1], DT[2], DT[3], CORRECT_SUB, DIRECTION, ACCESS, DES_ARRY[3], "", IP, "" ]
                            #print(SQL_ARRY)
                        else:
                            SQL_ARRY = [7, "COM_INTERFACE", "BACKUP", 0, "COM STANDARD NOT FOUND", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, "" ]
                            #print(SQL_ARRY)
                    else:
                        SQL_ARRY = [7, "COM_INTERFACE", "BACKUP", 0, "COM STANDARD NOT FOUND", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, "" ]
                        #print(SQL_ARRY)
                    return server.update(SQL_ARRY)
            elif (len(DES_ARRY) == 4):
                if (DES_ARRY[0]=='R'):
                    SQL_ARRY = [7, "COM_INTERFACE", "BACKUP", 0, "COM STANDARD NOT FOUND", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, "" ]
                    #print(SQL_ARRY)
                    return server.update(SQL_ARRY)
                elif (DES_ARRY[0]=='SYS') and (DES_ARRY[1]!='MGT'):
                    CORRECT_SUB = FIND_SUB(DES_ARRY[3])
                    if(CORRECT_SUB>0):
                        SQL_ARRY = [8, "COM_INTERFACE", "ACTIVE", 1, "STANDARD", DT[0], DT[1], DT[2], DT[3], CORRECT_SUB, DIRECTION, ACCESS, DES_ARRY[2], "", IP, "" ]
                        #print(SQL_ARRY)
                    else:
                        SQL_ARRY = [8, "COM_INTERFACE", "ACTIVE", 0, "COM STANDARD NOT FOUND", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, "" ]
                        #print(SQL_ARRY)
                    return server.update(SQL_ARRY)
            elif (DES_ARRY[0]=='R'):
                SQL_ARRY = [7, "COM_INTERFACE", "BACKUP", 0, "COM STANDARD NOT FOUND", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, "" ]
                #print(SQL_ARRY)
                return server.update(SQL_ARRY)
        elif (FIND_COMMON(DES_ARRY)>0):
            SQL_ARRY = [6, "COM_INTERFACE", "NONE", 0, "COM STANDARD NOT FOUND", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, "" ]
            #print(SQL_ARRY)
            return server.update(SQL_ARRY)
        return 0
    except ValueError: return 0
    except IndexError: return 0

################################## 
def OTHER_INTERFACE(DIRECTION, ACCESS, SUB, CX, IP, DT):
    try:
        SQL_ARRY = []
        SQL_ARRY = [11, "OTHER_INTERFACE", "NONE", 0, "NOT STANDARD", DT[0], DT[1], DT[2], DT[3], SUB, DIRECTION, ACCESS, CX, "", IP, "" ]
        #print(SQL_ARRY)
        return server.update(SQL_ARRY)
    except ValueError: return 0
    except IndexError: return 0

################################## 
def EMPTY_INTERFACE(DT):
    try:
        SQL_ARRY = []
        SQL_ARRY = [10, "EMPTY_INTERFACE", "EMPTY", 0, "NOT STANDARD", DT[0], DT[1], DT[2], DT[3], "", "", "", "", "", "", "" ]
        #print(SQL_ARRY)
        return server.update(SQL_ARRY)
    except ValueError: return 0
    except IndexError: return 0


