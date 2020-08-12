import datetime
import os

def write_data(DATA):
    REPORT_DATE = str(datetime.datetime.now().date())
    ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
    FILE = ABSOLUTE_PATH + "\logs\LOG_"+REPORT_DATE+".log"
    #print(FILE)
    #FILE = "logs/LOG_"+REPORT_DATE+".ims"
    with open(FILE,"a+") as vpncd_file:
        now_date_time = datetime.datetime.now()
        vpncd_file.write( str(now_date_time)+" : "+DATA+"\r\n")
        
#if __name__ == '__main__':
#    write_data("Hellow")
