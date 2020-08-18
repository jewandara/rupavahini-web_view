#################################################################
######################## Sira Version 2.0.1 #####################
#################################################################

from netmiko import ConnectHandler
import re
import datetime
import validateData
import os

class __DEVICE:
    def __init__(self, _JUMP_SERVER_CONFIG, _DOMAIN_USER_CONFIG, _DEVICE_DATA):
        # CONFIGERATION DECLARATION
        self.SERVER_SESSION = []
        self.ENABLE = []
        self.WRITE_OUT = ""
        # DEVICE DATA DECLARATION
        self.JUMP_SERVER_CONFIG_IN = _JUMP_SERVER_CONFIG["in"]
        self.JUMP_SERVER_CONFIG_OUT = _JUMP_SERVER_CONFIG["out"]
        self.DOMAIN_USER_CONFIG_USERNAME = _DOMAIN_USER_CONFIG["username"]
        self.DOMAIN_USER_CONFIG_PASSWORD = _DOMAIN_USER_CONFIG["password"]
        self.DOMAIN_USER_CONFIG_SYNC_MYSQL_DB = _DOMAIN_USER_CONFIG["syncMysqlDB"]
        self.DOMAIN_USER_CONFIG_SYNC_MONGO_DB = _DOMAIN_USER_CONFIG["syncMongoDB"]
        # DEVICE DATA DECLARATION
        self.DEVICE_ID = _DEVICE_DATA[0]
        self.DEVICE_TYPE = _DEVICE_DATA[1]
        self.DEVICE_IP = _DEVICE_DATA[2]
        self.DEVICE_NAME = _DEVICE_DATA[3]
        self.DEVICE_HOST_NAME = _DEVICE_DATA[4]
        self.DEVICE_BRAND = _DEVICE_DATA[5]
        self.DEVICE_CATEGORY = _DEVICE_DATA[6]
        self.DEVICE_POSITION = _DEVICE_DATA[7]
        self.DEVICE_SYMBOLE = _DEVICE_DATA[8]
        self.DEVICE_USER = _DEVICE_DATA[9]
        self.DEVICE_PASS = _DEVICE_DATA[10]
        self.DEVICE_PROTOCOL = _DEVICE_DATA[11]
        self.DEVICE_ACTIVE = _DEVICE_DATA[12]
        self.DEVICE_STATUS = _DEVICE_DATA[13]
        self.DEVICE_UNIQUE_VENDOR = _DEVICE_DATA[1]
    #########################################################################
    #########################################################################
    #########################################################################


    #########################################################################
    def _JUMP(self):
        try:
            self.SERVER_SESSION = ConnectHandler(**self.JUMP_SERVER_CONFIG_IN)
            OUT = self.SERVER_SESSION.send_command_timing(' ', strip_command=False, strip_prompt=False)
            JUMP_AFTER_AT = validateData.SPLIST("@", OUT)
            if(JUMP_AFTER_AT[1] == str(self.JUMP_SERVER_CONFIG_OUT)): return [1, 'JUMP_D', 'Login to jump server is successful.']
            else: return [0, 'JUMP_F', 'After login string is not equal.']
        except Exception as error:
            return [0, 'JUMP_E', str(error)]
        
    #########################################################################
    def _CHECK_JUMP(self):
        try:
            OUT = self.SERVER_SESSION.send_command_timing('\x036\n', strip_command=False, strip_prompt=False)
            OUT = self.SERVER_SESSION.send_command_timing('\x036\n', strip_command=False, strip_prompt=False)
            OUT = self.SERVER_SESSION.send_command_timing('\x036\n', strip_command=False, strip_prompt=False)
            OUT = self.SERVER_SESSION.send_command_timing(' ', strip_command=False, strip_prompt=False)
            #print(OUT)
            JUMP_AFTER_AT = validateData.SPLIST("@", OUT)
            if(JUMP_AFTER_AT[1] == str(self.JUMP_SERVER_CONFIG_OUT)): return 1
            else: return 0
        except: return 0

    #########################################################################
    def _RETURN_TO_JUMP(self, _DEVICE_DATA):
        try:
            # DEVICE DATA DECLARATION
            self.DEVICE_ID = _DEVICE_DATA[0]
            self.DEVICE_TYPE = _DEVICE_DATA[1]
            self.DEVICE_IP = _DEVICE_DATA[2]
            self.DEVICE_NAME = _DEVICE_DATA[3]
            self.DEVICE_HOST_NAME = _DEVICE_DATA[4]
            self.DEVICE_BRAND = _DEVICE_DATA[5]
            self.DEVICE_CATEGORY = _DEVICE_DATA[6]
            self.DEVICE_POSITION = _DEVICE_DATA[7]
            self.DEVICE_SYMBOLE = _DEVICE_DATA[8]
            self.DEVICE_USER = _DEVICE_DATA[9]
            self.DEVICE_PASS = _DEVICE_DATA[10]
            self.DEVICE_PROTOCOL = _DEVICE_DATA[11]
            self.DEVICE_ACTIVE = _DEVICE_DATA[12]
            self.DEVICE_STATUS = _DEVICE_DATA[13]
            self.DEVICE_UNIQUE_VENDOR = _DEVICE_DATA[1]

            if(self._CHECK_JUMP()): return [1, 'RETURN_JUMP_D', 'Return to jump server is successful.']
            else:
                OUT = self.SERVER_SESSION.send_command_timing('exit\n', strip_command=False, strip_prompt=False)
                if(self._CHECK_JUMP()): return [1, 'RETURN_JUMP_D', 'Return to jump server is successful.']
                else:
                    OUT = self.SERVER_SESSION.send_command_timing('exit\n', strip_command=False, strip_prompt=False)
                    if(self._CHECK_JUMP()): return [1, 'RETURN_JUMP_D', 'Return to jump server is successful.']
                    else:
                        OUT = self.SERVER_SESSION.send_command_timing('exit\n', strip_command=False, strip_prompt=False)
                        if(self._CHECK_JUMP()): return [1, 'RETURN_JUMP_D', 'Return to jump server is successful.']
                        else: return [0, 'RETURN_JUMP_F', 'Faild to return jump server.' ]
        except Exception as error:
            return [0, 'RETURN_JUMP_E', str(error)]

    #########################################################################
    def _TELNET(self):
        try:
            OUT = self.SERVER_SESSION.send_command_expect( 'telnet ' + str(self.DEVICE_IP), 'Username')
            OUT += self.SERVER_SESSION.send_command_expect( str(self.DOMAIN_USER_CONFIG_USERNAME), 'Password')
            OUT += self.SERVER_SESSION.send_command_timing( str(self.DOMAIN_USER_CONFIG_PASSWORD) + '\n', normalize=False)
            return [1, 'TELNET_D', 'Running telnet is successful.']
        except Exception as error:
            return [0, 'TELNET_E', str(error)]

    #########################################################################
    def _SSH(self):
        try:
            OUT = self.SERVER_SESSION.send_command_timing( 'ssh '+str(self.DEVICE_USER)+'@'+str(self.DEVICE_IP)+'\n', normalize=False)
            OUT = self.SERVER_SESSION.send_command_timing( str(self.DEVICE_PASS)+'\n', normalize=False)
            OUT = self.SERVER_SESSION.send_command_timing( '\n', normalize=False)
            if(OUT[-1] == '>'): return [1, 'SSH_D', 'Running ssh is successful.']
            else:
                OUT = self.SERVER_SESSION.send_command_timing( '\n\n\n\n\n\n\n', normalize=False)
                OUT = self.SERVER_SESSION.send_command_timing( 'ssh '+str(self.DEVICE_USER)+'@'+str(self.DEVICE_IP)+'\n', normalize=False)
                OUT = self.SERVER_SESSION.send_command_timing( 'yes\n', normalize=False)
                OUT = self.SERVER_SESSION.send_command_timing( str(self.DEVICE_PASS)+'\n', normalize=False)
                OUT = self.SERVER_SESSION.send_command_timing( '\n', normalize=False)
                if(OUT[-1] == '>'): return [1, 'SSH_D', 'Running ssh is successful.']
                else: return [0, 'SSH_F', 'After login has no  ">" symbol.']
        except Exception as error:
            return [0, 'SSH_E', str(error)]

    #########################################################################
    def _ROUTER_TYPE(self):
        try:
            DATA = self.SERVER_SESSION.send_command_timing( '\n', normalize=False)
            ROUTER_HOST_NAME = re.findall('<(.*?)>', DATA, re.DOTALL)
            if(ROUTER_HOST_NAME!=[]): EN = [1, "HUAWEI", 0, ROUTER_HOST_NAME[0]]
            else:
                ROUTER_HOST_NAME = re.findall('\[(.*?)\]', DATA, re.DOTALL)
                if(ROUTER_HOST_NAME!=[]): EN = [1, "HUAWEI", 1, ROUTER_HOST_NAME[0]]
                else:
                    ROUTER_HOST_NAME = re.findall('(.*?)>', DATA, re.DOTALL)
                    if(ROUTER_HOST_NAME!=[]): EN = [1, "CISCO", 0, ROUTER_HOST_NAME[0]]
                    else:
                        ROUTER_HOST_NAME = re.findall('(.*?)#', DATA, re.DOTALL)
                        if(ROUTER_HOST_NAME!=[]): EN = [1, "CISCO", 1, ROUTER_HOST_NAME[0]]
                        else: EN = [0, "UNKNOWN", 0, self.DEVICE_IP]
            if(EN[3]=='.'): EN = [0, "NO_ACCESS", 0, self.DEVICE_IP]
            return [1, 'ROUTER_TYPE_D', EN]
        except Exception as error:
            return [0, 'ROUTER_TYPE_E', str(error)]

    #########################################################################
    def _ENABLE_MODE(self):
        try:
            ROUTER_TYPE = self._ROUTER_TYPE()
            if(ROUTER_TYPE[0]):
                EN = ROUTER_TYPE[2]
                if(EN[2]):
                    self.ENABLE = EN
                    return [1, 'ENABLE_MODE_D', 'Access enable mode is successful.']
                else:
                    if(self.DEVICE_BRAND=="HUAWEI"):
                        OUT = self.SERVER_SESSION.send_command_timing("system-view\n", normalize=False)
                        OUT += self.SERVER_SESSION.send_command_timing( str(self.DEVICE_PASS) + '\n', normalize=False)
                        ROUTER_TYPE = self._ROUTER_TYPE()
                        if(ROUTER_TYPE[0]):
                            EN = ROUTER_TYPE[2]
                            if(EN[2]):
                                self.ENABLE = EN
                                return [1, 'ENABLE_MODE_D', 'Access enable mode is successful.']
                            else: return [0, 'ENABLE_MODE_F', 'Cannot login to enable mode in HUAWEI router.']
                        else: return ROUTER_TYPE
                    elif(self.DEVICE_BRAND=="CISCO"):
                        OUT = self.SERVER_SESSION.send_command_timing("enable\n", normalize=False)
                        OUT += self.SERVER_SESSION.send_command_timing( str(self.DEVICE_PASS) + '\n', normalize=False)
                        ROUTER_TYPE = self._ROUTER_TYPE()
                        if(ROUTER_TYPE[0]):
                            EN = ROUTER_TYPE[2]
                            if(EN[2]):
                                self.ENABLE = EN
                                return [1, 'ENABLE_MODE_D', 'Access enable mode is successful.']
                            else: return [0, 'ENABLE_MODE_F', 'Cannot login to enable mode in CISCO router.']
                        else: return ROUTER_TYPE
                    else: return [0, 'ENABLE_MODE_F', 'Cannot find router module.']
            else: return ROUTER_TYPE
        except Exception as error:
            return [0, 'ENABLE_MODE_E', str(error)]

    #########################################################################
    def _CONFIG_MODE(self):
        try:
            if(self.ENABLE[1] == 'CISCO'):
                OUT = self.SERVER_SESSION.send_command_timing("configure terminal\n", normalize=False)
                OUT += self.SERVER_SESSION.send_command_timing('\n', normalize=False)
                CMODE_STRING = OUT[-10:-1].split("(",1)[1]
                if(CMODE_STRING == 'config)'): return [1, 'CONFIG_MODE_D', 'Access config mode is successful.']
                else: return [0, 'CONFIG_MODE_F', 'Access config mode is output string not matching.']
            elif(self.ENABLE[1] == 'HUAWEI'):
                OUT = self.SERVER_SESSION.send_command_timing("system-view\n", normalize=False)
                OUT += self.SERVER_SESSION.send_command_timing('\n', normalize=False)
                if(OUT[-1] == ']'): return [1, 'CONFIG_MODE_D', 'Access config mode is successful.']
                else: return [0, 'CONFIG_MODE_F', 'Access config mode is output string not matching.']
            else:
                OUT = self.SERVER_SESSION.send_command_timing("configure terminal\n", normalize=False)
                OUT += self.SERVER_SESSION.send_command_timing('\n', normalize=False)
                CMODE_STRING = OUT[-10:-1].split("(",1)[1]
                if(CMODE_STRING == 'config)'): return [1, 'CONFIG_MODE_D', 'Access config mode is successful.']
                else: return [0, 'CONFIG_MODE_F', 'Access config mode is output string not matching.']
        except Exception as error:
            return [0, 'CONFIG_MODE_E', str(error)]

    #########################################################################
    def _FIND_MORE(self, DATA):
        try:
            if(self.ENABLE[1] == 'HUAWEI'):
                DATA = re.sub(r'', '', DATA)
                DATA = re.sub(r'\[16D', '', DATA)
                DATA = re.sub(r'\[42D', '', DATA)
                DATA = re.sub(r' ---- More ----                                           ', '', DATA)
                DATA = re.sub(r'  ---- More ----                ', '', DATA)
                DATA = re.sub(r'---- More ----', '', DATA)
            else:
                DATA = re.sub(r'--More--            ', '', DATA)
                DATA = re.sub(r'--More--', '', DATA)
                DATA = re.sub(r'          ', '', DATA)
            self.WRITE_OUT = self.WRITE_OUT + DATA
            return [1, 'FIND_MORE_D', '']
        except Exception as error:
            return [0, 'FIND_MORE_E', str(error)]
        
    #########################################################################
    def _WRITE_DATA(self, COMMAND):
        try:
            if(self.ENABLE[1] == 'CISCO'):
                OUT = self.SERVER_SESSION.send_command_timing(str(COMMAND['CISCO']) + '\n', normalize=False)
                OUT += self.SERVER_SESSION.send_command_timing(" ", normalize=False)
            elif(self.ENABLE[1] == 'HUAWEI'):
                OUT = self.SERVER_SESSION.send_command_timing(str(COMMAND['HUAWEI']) + '\n', normalize=False)
                OUT += self.SERVER_SESSION.send_command_timing(" ", normalize=False)
            else:
                OUT = self.SERVER_SESSION.send_command_timing(str(COMMAND['OTHER']) + '\n', normalize=False)
                OUT += self.SERVER_SESSION.send_command_timing(" ", normalize=False)
            self.WRITE_OUT = self.WRITE_OUT + OUT
            return [1, 'WRITE_DATA_D', str(self.WRITE_OUT)]
        except Exception as error:
            return [0, 'WRITE_DATA_E', str(error)]

    #########################################################################
    def _WRITE_LONG_DATA(self, COMMAND):
        try:
            #-- DO --
            if(self.ENABLE[1] == 'CISCO'):
                OUT = self.SERVER_SESSION.send_command_timing(str(COMMAND['CISCO']) + '\n', normalize=False)
                OUT += self.SERVER_SESSION.send_command_timing(" ", normalize=False)
            elif(self.ENABLE[1] == 'HUAWEI'):
                OUT = self.SERVER_SESSION.send_command_timing(str(COMMAND['HUAWEI']) + '\n', normalize=False)
                OUT += self.SERVER_SESSION.send_command_timing(" ", normalize=False)
            else:
                OUT = self.SERVER_SESSION.send_command_timing(str(COMMAND['OTHER']) + '\n', normalize=False)
                OUT += self.SERVER_SESSION.send_command_timing(" ", normalize=False)
            self._FIND_MORE(OUT)
            #-- WHILE --
            while True:
                if "--More--" in OUT:
                    OUT = self.SERVER_SESSION.send_command_timing("                                                                                                                                                                                    ", normalize=False)
                    OUT += self.SERVER_SESSION.send_command_timing("                                                                                                                                                                                    ", normalize=False)
                    OUT += self.SERVER_SESSION.send_command_timing("                                                                                                                                                                                    ", normalize=False)
                    self._FIND_MORE(OUT)
                else: break
            return [1, 'WRITE_DATA_D', str(self.WRITE_OUT)]
        except Exception as error:
            return [0, 'WRITE_DATA_E', str(error)]


#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
############################  MAIN FUNCTION  ############################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
class NET(__DEVICE):
    def JUMP(self): return [ self._JUMP(), self.SERVER_SESSION, self.ENABLE ]
    def RETURN_JUMP(self, DEVICE): return [ self._RETURN_TO_JUMP(DEVICE), self.SERVER_SESSION, self.ENABLE ]
    def TELNET(self): return [ self._TELNET(), self.SERVER_SESSION, self.ENABLE ]
    def SSH(self): return [ self._SSH(), self.SERVER_SESSION, self.ENABLE ]
    def ENABLE_MODE(self): return [ self._ENABLE_MODE(), self.SERVER_SESSION, self.ENABLE ]
    def CONFIG_MODE(self): return [ self._CONFIG_MODE(), self.SERVER_SESSION, self.ENABLE ]
    def WRITE(self, COMMAND): return [ self._WRITE_DATA(COMMAND), self.SERVER_SESSION, self.ENABLE ]
    def WRITE_LONG(self, COMMAND): return [ self._WRITE_LONG_DATA(COMMAND), self.SERVER_SESSION, self.ENABLE ]
    
