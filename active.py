#import server
#import threading
#import requests
#from html_table_parser import HTMLTableParser



#def url_get_contents():
#    LOGIN_PAYLOAD = {'username': 'Rachitha_09415', 'password': '' }
#    with requests.Session() as sesn:
#        LOGIN_OUT = sesn.post('http://10.62.160.111/vpncd/index.php', data=LOGIN_PAYLOAD)
#        xhtml = sesn.get('http://10.62.160.111/vpncd/view_data.php?cid=', stream=True).content.decode('UTF-8')+"</td></tr></tbody></table>"
        #xhtml = sesn.get('http://10.62.160.111/vpncd/view_data.php?cid=', stream=True)
        #print(xhtml.encoding)
#        tableParser = HTMLTableParser()
#        tableParser.feed(xhtml)
#        return tableParser.tables[0]

#def main():
#    print("-------------------------------")
#    print("---START SEARCH ACTIVE LINKS")
#    print("-------------------------------")
#    print("---LOADING VPNCD DATA . . .WAIT . . .")
#    tableArry = url_get_contents()
#    COUNT = len(tableArry)
#    print("---TOTAL VPNCD COUNT : ", COUNT)
    #print("---DELETEING PREVIEST VPNCD DATA . . .WAIT . . .")

    #server.set_run_sql("DELETE FROM `vpncd_session_tb`")
    #print("---EMPTY PREVIEST DATA")
    #print("---ADDING NEW ACTIVE SESSION")
    #for i in range(1, COUNT-1):
        #tr = tableArry[i]
        ##server.set_run_sql("INSERT INTO `vpncd_session_tb` (`DID`) VALUES (( SELECT ALLD.DID FROM all_data_view AS ALLD WHERE ALLD.DESCRIPTION = '"+tr[0]+"' AND ALLD.PE_IP = '"+tr[2]+"' AND ALLD.INTERFACE = '"+tr[3]+"' LIMIT 1 )); ")
        #server.set_run_sql("INSERT INTO `vpncd_session_tb` (`des`, `inter`, `ip`) VALUES ('"+tr[0]+"', '"+tr[3]+"', '"+tr[2]+"'); ")
        #print("---SESSION:", i)
    #print("---NEW SESSION INTERFACES ADDED :", COUNT)
    #print("---SUCCESSFULLY UPDATED ALL REFERENCE")
    #print("-------------------------------")
#    return 1

#if __name__ == '__main__':
#     thread = threading.Thread(target=main)
#     thread.start()
#     thread.join()
