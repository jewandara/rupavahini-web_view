############################################################
######################## Version 2.0.1 #####################
############################################################

import requests
import requests.auth
import os

class __config:
    def __init__(self, _URL_DATA):
        self._URL_REQUEST = _URL_DATA["URL_REQUEST"]
        self._URL_TYPE = _URL_DATA["URL_TYPE"]
        self._URL_CATA = _URL_DATA["URL_CATA"]
        self._RETURN_DATA = []
        self._SESSION_DATA = self._CALLING_URL(self._URL_REQUEST)

    def _GET_URL_DATA(self):
        try: return self._SESSION_DATA
        except Exception as error: return [0, "GETTING SESSION ERROR", error]

    def _CALLING_URL(self, REQUEST_DATA):
        try:
            if(self._URL_TYPE == "POST"):
                if(self._URL_CATA == "DATA"):
                    self._RETURN_DATA = requests.post(str(REQUEST_DATA["URL"]), data=REQUEST_DATA["DATA"])
                elif(self._URL_CATA == "JSON"):
                    self._RETURN_DATA = requests.post(str(REQUEST_DATA["URL"]), json=REQUEST_DATA["DATA"])
                elif(self._URL_CATA == "FILE"):
                    self._RETURN_DATA = requests.post(str(REQUEST_DATA["URL"]), files=REQUEST_DATA["DATA"])
                else:
                    self._RETURN_DATA = requests.post(str(REQUEST_DATA["URL"]), data=REQUEST_DATA["DATA"])
            else:
                self._RETURN_DATA = requests.get(str(REQUEST_DATA["URL"]))
            return [1, self._RETURN_DATA, self._RETURN_DATA.text]
        except Exception as error: return [0, "URL CALLING POST ERROR", error]



class urlRequest(__config):
    def URL(self): return self._GET_URL_DATA()
    def CALL(self, REQUEST_DATA): return self._CALLING_URL(REQUEST_DATA)



############################################################
######################## Version 2.0.1 #####################
############################################################

#DATA = {
#    "URL_REQUEST":{
#        "URL" : "http://10.62.96.8:8089/onecrm/getconnectionstatus?number=994620782",
#        "DATA" : ""
#        },
#    "URL_TYPE": "GET",
#    "URL_CATA": "DATA"
#    }

#mail = urlRequest(DATA)
#RESUT = mail.URL()
#print(RESUT)
#RESUT = mail.CALL({"URL" : "http://10.62.96.8:8089/onecrm/getconnectionstatus?number=994633061", "DATA" : ""})
#print(RESUT)

############################################################
