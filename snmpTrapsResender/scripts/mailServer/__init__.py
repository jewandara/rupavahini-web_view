############################################################
######################## Version 2.0.1 #####################
############################################################

import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import formatdate
from email import encoders
import datetime

class __config:
    def __init__(self, _MAIL_SERVER):
        self._SERVER = _MAIL_SERVER["server"]
        self._PORT = _MAIL_SERVER["port"]
        self._SENDER = "SIRA DEVELOPMENT <sira@dialog.lk>"

    def _SENDING_EMAIL(self, _SENDING_DATA):
        try:
            NOW_DATE = str(datetime.datetime.now().date())
            MAIL_MSG = MIMEMultipart('alternative')
            #To
            if((_SENDING_DATA["To"]!=[]) and (_SENDING_DATA["To"][0]!="") and (_SENDING_DATA["To"][0]!="Null")):
                SEND_TO_STRING = ", ".join(_SENDING_DATA["To"])
                MAIL_MSG['To'] = str(SEND_TO_STRING)
            else: return [0, "MAIL SEND ERROR", "Can not find sending email address"]
            #Cc
            if((_SENDING_DATA["Cc"]!=[]) and (_SENDING_DATA["Cc"][0]!="") and (_SENDING_DATA["Cc"][0]!="Null")):
                SEND_TO_STRING = ", ".join(_SENDING_DATA["Cc"])
                MAIL_MSG['Cc'] = str(SEND_TO_STRING)
            #From
            MAIL_MSG['From'] = self._SENDER
            #Subject
            if((_SENDING_DATA["Subject"]!="") and (_SENDING_DATA["Subject"]!="Null")):
                MAIL_MSG['Subject'] = str(_SENDING_DATA["Subject"])
            else: MAIL_MSG['Subject'] = "TEST EMIL: "+NOW_DATE
            MAIL_MSG['MIME-Version'] = "1.0"
            MAIL_MSG['Content-type'] = "text/html; charset=iso-8859-1\r\n\r\n"
            #Body
            if((_SENDING_DATA["Body"]!="") and (_SENDING_DATA["Body"]!="Null")):
                MAIL_BODY  = MIMEText(str(_SENDING_DATA["Body"]), 'html')
            else: MAIL_BODY  = MIMEText("<h2>This is test E-mail. Please ignore this mail.</h2>", 'html')
            MAIL_MSG.attach(MAIL_BODY)
            #Attachment
            if((_SENDING_DATA["Attachment"]!=[]) and (_SENDING_DATA["Attachment"]!="") and (_SENDING_DATA["Attachment"]!="Null")):
                MAIL_ATTACH = MIMEBase('application', "octet-stream")
                ATTACHED_PATH = str(_SENDING_DATA["Attachment"]["filepath"])
                MAIL_ATTACH.set_payload(open(ATTACHED_PATH, "rb").read())
                encoders.encode_base64(MAIL_ATTACH)
                MAIL_ATTACH.add_header('Content-Disposition', 'attachment; filename="'+str(_SENDING_DATA["Attachment"]["filename"])+'"')
                MAIL_MSG.attach(MAIL_ATTACH)
            #SENDER
            server = smtplib.SMTP(self._SERVER, self._PORT)
            for mail_address in _SENDING_DATA["To"]:
                server.sendmail(self._SENDER, str(mail_address), MAIL_MSG.as_string())
            for mail_address in _SENDING_DATA["Cc"]:
                server.sendmail(self._SENDER, str(mail_address), MAIL_MSG.as_string())
            server.quit()
            return [1, 'SENDING MAIL SUCCESSFULLY', server]
        except Exception as error: return [0, 'FAILD SENDING MAIL', str(error) ]


class mailServer(__config):
    def SEND(self, body): return self._SENDING_EMAIL(body)





############################################################
######################## Version 2.0.1 #####################
############################################################

# DIALOG_MAIL_SERVER = {'server': 'spamfiltpriv.dialog.lk', 'port': 25 }
# DATA = {
#    "Subject":"TEST EMAIL SEND",
#    "To": [ "Rachitha <rachitha.jeewandara@dialog.lk>" ],
#    "Cc": [],
#    "Body":"",
#    "Attachment": {
#                    "filepath":"C:/Users/Rachitha_09415/Desktop/PROT DESCRIPTION_PROJECT/CSR.xlsx",
#                    "filename":"PROT DESCRIPTION_PROJECT.xlsx"
#                    }
#    }
#SESSION = mailServer.EMAIL(DIALOG_MAIL_SERVER)
#RESUT = SESSION.SEND(DATA)

############################################################
