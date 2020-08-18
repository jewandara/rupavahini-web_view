import datetime
import xlwt
import os

def doc(FOLDER, NAME, DATA, PATH = ''):
    try:
        NOW_DATETIME = datetime.datetime.now()
        if(PATH == ''):
            ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
            ABSOLUTE_PATH = ABSOLUTE_PATH.replace("scripts", "DATA")
            DOC_PATH = ABSOLUTE_PATH.replace("writeData", "doc")
            REQUEST_PATH = DOC_PATH+"\\"+FOLDER
            if not os.path.exists(DOC_PATH): os.mkdir(DOC_PATH)
            if not os.path.exists(REQUEST_PATH): os.mkdir(REQUEST_PATH)
            FILE = REQUEST_PATH+"\\"+NAME+".impls"
        else:
            REQUEST_PATH = PATH+"\\"+FOLDER
            if not os.path.exists(REQUEST_PATH): os.mkdir(REQUEST_PATH)
            FILE = REQUEST_PATH+"\\"+NAME+".impls"   
        with open(FILE,"a+") as impls:
            impls.write("\n\n\n")
            impls.write("------------------------------------------------------------------------------------------------\n")
            impls.write("-----------------------------------"+str(NOW_DATETIME)+"-----------------------------------\n")
            impls.write("------------------------------------------------------------------------------------------------\n")
            impls.write("\n\n"+DATA)
        return [1, 'CREATING DOC FILE SUCCESSFULLY', FILE ]
    except Exception as error:
        return [0, 'CREATING DOC FILE ERROR OCCERED', str(error) ]

def config(TYPE, DEVICE, DATA, PATH = ''):
    try:
        REPORT_DATE = str(datetime.datetime.now().date())
        if(PATH == ''):
            ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
            ABSOLUTE_PATH = ABSOLUTE_PATH.replace("scripts", "DATA")
            CONFIG_PATH = ABSOLUTE_PATH.replace("writeData", "config")
            TYPE_PATH = CONFIG_PATH+"\\"+TYPE
            REQUEST_PATH = TYPE_PATH+"\\"+DEVICE
            if not os.path.exists(CONFIG_PATH): os.mkdir(CONFIG_PATH)
            if not os.path.exists(TYPE_PATH): os.mkdir(TYPE_PATH)
            if not os.path.exists(REQUEST_PATH): os.mkdir(REQUEST_PATH)
            FILE = REQUEST_PATH + "/"+REPORT_DATE+".config"
        else:
            TYPE_PATH = PATH+"\\"+TYPE
            REQUEST_PATH = TYPE_PATH+"\\"+DEVICE
            if not os.path.exists(TYPE_PATH): os.mkdir(TYPE_PATH)
            if not os.path.exists(REQUEST_PATH): os.mkdir(REQUEST_PATH)
            FILE = REQUEST_PATH + "/"+REPORT_DATE+".config"
        with open(FILE,"a+") as config:
            config.write(DATA)
        return [1, 'CREATING CONFIG FILE SUCCESSFULLY', FILE ]
    except Exception as error:
        return [0, 'CREATING CONFIG FILE ERROR OCCERED', str(error) ]

def logs(DATA, PATH = ''):
    try:
        REPORT_DATE = str(datetime.datetime.now().date())
        if(PATH == ''):
            ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
            ABSOLUTE_PATH = ABSOLUTE_PATH.replace("scripts", "DATA")
            REQUEST_PATH = ABSOLUTE_PATH.replace("writeData", "logs")
            if not os.path.exists(REQUEST_PATH): os.mkdir(REQUEST_PATH)
            FILE = REQUEST_PATH + "/"+REPORT_DATE+".log"
        else:
            FILE = PATH + "/"+REPORT_DATE+".log"
        with open(FILE,"a+") as log:
            NOW_DATETIME = datetime.datetime.now()
            log.write( str(NOW_DATETIME)+"\t:\t"+DATA+"\r\n")
        return [1, 'CREATING LOG FILE SUCCESSFULLY', FILE ]
    except Exception as error:
        return [0, 'CREATING LOG FILE ERROR OCCERED', str(error) ]

def excel(DATA, PATH = ''):
    try:
        tittle_font = 'font: height 220, name Calibri, colour_index black, bold on;'
        tittle_align = 'align: wrap on, vert centre, horiz center;'
        tittle_borders = 'borders: top thin, bottom thin, left thin, right thin;'
        tittle_pattern = 'pattern: pattern solid, fore_colour yellow;'

        table_id_colom_font = 'font: height 180, name Arial, colour_index light_blue, italic on;'
        table_id_colom_align = 'align: wrap on, vert centre, horiz left;'
        table_id_colom_borders = 'borders: top thin, bottom thin, left thin, right thin;'
        table_id_colom_pattern = 'pattern: pattern solid, fore_colour white;'

        table_colom_font = 'font: height 190, name Arial, colour_index black;'
        table_colom_align = 'align: vert centre, horiz left;'
        table_colom_borders = 'borders: top thin, bottom thin, left thin, right thin;'
        table_colom_pattern = 'pattern: pattern solid, fore_colour white;'

        tittle_style = xlwt.easyxf(tittle_pattern + tittle_borders + tittle_align + tittle_font)
        table_id_colom_style = xlwt.easyxf(table_id_colom_pattern + table_id_colom_borders + table_id_colom_align + table_id_colom_font)
        table_colom_style = xlwt.easyxf(table_colom_pattern + table_colom_borders + table_colom_align + table_colom_font)

        wbook = xlwt.Workbook()
        for SHEETS in DATA["SHEETS"]:
            wsheet = wbook.add_sheet(SHEETS["NAME"])
            wsheet.write(0, 0, "_ID", tittle_style)
            #TITTLE
            i = 0
            for TITTLE in SHEETS["TITTLE"]:
                i = i + 1
                wsheet.write(0, i, str(TITTLE), tittle_style)
            #BODY
            j = 0
            for ROW in SHEETS["DATA"]:
                k = 0
                j = j + 1
                wsheet.write(j, k, j, table_id_colom_style)
                for CEL in ROW:
                    k = k + 1
                    wsheet.write(j, k, str(CEL), table_colom_style)
        REPORT_DATE = str(datetime.datetime.now().date())
        if(PATH == ''):
            ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
            ABSOLUTE_PATH = ABSOLUTE_PATH.replace("scripts", "DATA")
            REQUEST_PATH = ABSOLUTE_PATH.replace("writeData", "excel")
            if not os.path.exists(REQUEST_PATH): os.mkdir(REQUEST_PATH)
            FILE = REQUEST_PATH + "/"+REPORT_DATE+"_"+DATA["FILE"]+".xls"
        else:
            FILE = PATH + "/"+REPORT_DATE+"_"+DATA["FILE"]+".xls"
        wbook.save(str(FILE))
        return [1, 'CREATING EXCEL FILE SUCCESSFULLY', FILE ]
    except Exception as error:
        return [0, 'CREATING EXCEL FILE ERROR OCCERED', str(error) ]
























#######################################################################
#          data = {
#                    "FILE":"TEST_TAC",
#                    "SHEETS": [
#                         {
#                              "NAME":"BOOK_ONE",
#                              "TITTLE":[ "TITLE One", "TITLE Two","TITLE Three","TITLE Four","TITLE Five" ],
#                              "DATA":[ [ "One", "Two","Three","Four","Five" ], [ "ABC", "DER","GHJ","IUY","TYU" ], [ "ERT", "BNM","RFG","PJG","XIY" ], [ "ASTD","DHTS","TITL","TEAS","EWSA" ] ] 
#                         },
#                         {
#                              "NAME":"BOOK_TWO",
#                              "TITTLE":[ "TITLE One", "TITLE Two","TITLE Three","TITLE Four","TITLE Five" ],
#                              "DATA":[ [ "One", "Two","Three","Four","Five" ], [ "ABC", "DER","GHJ","IUY","TYU" ], [ "ERT", "BNM","RFG","PJG","XIY" ], [ "ASTD","DHTS","TITL","TEAS","EWSA" ] ]
#                         }
#                    ]
#          }
#          result = writeData.excel(data)
#          print(result)
#
#
#######################################################################
#
#result = writeData.doc("test2", "dddd", "Hellow\nsdfsdf\n sdfsd")
#print(result)
#
#
#
#######################################################################
#
#result = writeData.config("BE", "KALA_TEST_01", "fgdfgdfgdfgdfgsdfsd")
#print(result)
#
#
#
#
#######################################################################
#
#result = writeData.logs("BEfgdfgd fgdfgdfgsdfsd done")
#print(result)
#
#
#######################################################################
