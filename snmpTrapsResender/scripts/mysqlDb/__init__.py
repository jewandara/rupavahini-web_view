#################################################################
######################## Sira Version 2.0.1 #####################
#################################################################

import os
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

class __database:
    def __init__(self, dname="mpls_db", hname="localhost", uname="root", pname=""):
        self.host_name = hname
        self.user_name = uname
        self.pass_word = pname
        self.db_name = dname
    ####################################
    def _add(self, table, data):
        try:
            RE = []
            os.environ['NO_PROXY'] = 'localhost'
            connection = mysql.connector.connect(host=self.host_name, user=self.user_name, passwd=self.pass_word, database=self.db_name)
            cursor = connection.cursor()
            query = "INSERT INTO "+str(table)+" VALUES "+str(data)+" "
            cursor.execute(query)
            ID = cursor.lastrowid
            connection.commit()
            connection.rollback()
            del cursor
            if (connection.is_connected()):  connection.close()
            return [1, 'INSERTING A NEW RECORD TO MYSQL DATABASE SUCCESSFULLY (_add)', ID ]
        except mysql.connector.Error as error:
            return [0, 'SQL ERROR AND FAILED INSERTING A NEW RECORD TO SQL DATABASE (_add)', format(error)]
        except Exception as error:
            return [0, 'EXCEPTION AND FAILED INSERTING A NEW RECORD TO SQL DATABASE (_add)', format(error)]
    ####################################
    def _addList(self, table, data):
        try:
            RE = []
            os.environ['NO_PROXY'] = 'localhost'
            connection = mysql.connector.connect(host=self.host_name, user=self.user_name, passwd=self.pass_word, database=self.db_name)
            cursor = connection.cursor()
            query = "INSERT INTO "+str(table)+" VALUES "+str(data)+" "
            cursor.execute(query)
            IDS = [ cursor.lastrowid, cursor.rowcount]
            connection.commit()
            connection.rollback()
            del cursor
            if (connection.is_connected()):  connection.close()
            return [1, 'INSERTING NEW RECORDS TO MYSQL DATABASE SUCCESSFULLY (_addList)', IDS ]
        except mysql.connector.Error as error:
            return [0, 'SQL ERROR AND FAILED INSERTING NEW RECORDS TO SQL DATABASE (_addList)', format(error)]
        except Exception as error:
            return [0, 'EXCEPTION AND FAILED INSERTING NEW RECORDS TO SQL DATABASE (_addList)', format(error)]
    ####################################
    def _view(self, table, data):
        try:
            RE = []
            os.environ['NO_PROXY'] = 'localhost'
            connection = mysql.connector.connect(host=self.host_name, user=self.user_name, passwd=self.pass_word, database=self.db_name)
            cursor = connection.cursor()
            query = "SELECT * FROM "+str(table)+" WHERE "+str(data)+" LIMIT 1"
            cursor.execute(query)
            result = cursor.fetchall()
            if(result == []): RE = [[], 0]
            else: RE = [result, cursor.rowcount]
            connection.commit()
            connection.rollback()
            del cursor
            if (connection.is_connected()):  connection.close()
            return [1, 'VIEWING RECORDS IN MYSQL DATABASE SUCCESSFULLY (_view)', RE ]
        except mysql.connector.Error as error:
            return [0, 'SQL ERROR AND FAILED VIEWING RECORDS IN SQL DATABASE (_view)', format(error)]
        except Exception as error:
            return [0, 'EXCEPTION AND FAILED VIEWING RECORDS IN SQL DATABASE (_view)', format(error)]
    ####################################
    def _viewAll(self, table, data):
        try:
            RE = []
            os.environ['NO_PROXY'] = 'localhost'
            connection = mysql.connector.connect(host=self.host_name, user=self.user_name, passwd=self.pass_word, database=self.db_name)
            cursor = connection.cursor()
            query = "SELECT * FROM "+str(table)+" WHERE "+str(data)+" "
            cursor.execute(query)
            result = cursor.fetchall()
            if(result == []): RE = [[], 0]
            else: RE = [result, cursor.rowcount]
            connection.commit()
            connection.rollback()
            del cursor
            if (connection.is_connected()):  connection.close()
            return [1, 'VIEWING ALL RECORDS IN MYSQL DATABASE SUCCESSFULLY (_viewAll)', RE ]
        except mysql.connector.Error as error:
            return [0, 'SQL ERROR AND FAILED VIEWING ALL RECORDS IN SQL DATABASE (_viewAll)', format(error)]
        except Exception as error:
            return [0, 'EXCEPTION AND FAILED VIEWING ALL RECORDS IN SQL DATABASE (_viewAll)', format(error)]
    ####################################
    def _edit(self, table, data, option):
        try:
            RE = []
            os.environ['NO_PROXY'] = 'localhost'
            connection = mysql.connector.connect(host=self.host_name, user=self.user_name, passwd=self.pass_word, database=self.db_name)
            cursor = connection.cursor()
            query = "UPDATE "+str(table)+" SET "+str(data)+" WHERE "+str(option)
            cursor.executemany(query, data)
            RE = cursor.rowcount
            connection.commit()
            connection.rollback()
            del cursor
            if (connection.is_connected()):  connection.close()
            return [1, 'EDITING RECORDS IN MYSQL DATABASE SUCCESSFULLY (_edit)', RE ]
        except mysql.connector.Error as error:
            return [0, 'SQL ERROR AND FAILED EDITING RECORDS IN SQL DATABASE (_edit)', format(error)]
        except Exception as error:
            return [0, 'EXCEPTION AND FAILED EDITING RECORDS IN SQL DATABASE (_edit)', format(error)]
    ####################################
    def _editId(self, table, key, data):
        try:
            RE = []
            os.environ['NO_PROXY'] = 'localhost'
            connection = mysql.connector.connect(host=self.host_name, user=self.user_name, passwd=self.pass_word, database=self.db_name)
            cursor = connection.cursor()
            query = "UPDATE "+str(table)+" SET "+str(key)
            print(query)
            cursor.executemany(query, data)
            RE = cursor.rowcount
            connection.commit()
            connection.rollback()
            del cursor
            if (connection.is_connected()):  connection.close()
            return [1, 'EDITING RECORDS BY ID IN MYSQL DATABASE SUCCESSFULLY (_editId)', RE ]
        except mysql.connector.Error as error:
            return [0, 'SQL ERROR AND FAILED EDITING RECORDS BY ID IN SQL DATABASE (_editId)', format(error)]
        except Exception as error:
            return [0, 'EXCEPTION AND FAILED EDITING RECORDS BY ID IN SQL DATABASE (_editId)', format(error)]
    ####################################
    def _deleteBy(self, table, data):
        try:
            RE = []
            os.environ['NO_PROXY'] = 'localhost'
            connection = mysql.connector.connect(host=self.host_name, user=self.user_name, passwd=self.pass_word, database=self.db_name)
            cursor = connection.cursor()
            query = "DELETE FROM "+str(table)+" WHERE "+str(data)
            #print(query)
            cursor.execute(query)
            RE = cursor.rowcount
            connection.commit()
            connection.rollback()
            del cursor
            if (connection.is_connected()):  connection.close()
            return [1, 'DELETING RECORDS IN MYSQL DATABASE SUCCESSFULLY (_deleteBy)', RE ]
        except mysql.connector.Error as error:
            return [0, 'SQL ERROR AND FAILED DELETING RECORDS IN SQL DATABASE (_deleteBy)', format(error)]
        except Exception as error:
            return [0, 'EXCEPTION AND FAILED EDITING RECORDS IN SQL DATABASE (_deleteBy)', format(error)]
    ####################################
   

class mysqlDb(__database):
   def add(self, table, data): return self._add(table, data) 
   def addList(self, table, data): return self._addList(table, data) 
   def view(self, table, data="1=1"): return self._view(table, data)
   def viewAll(self, table, data="1=1"): return self._viewAll(table, data)
   def edit(self, table, data, option="1=1"): return self._edit(table, data, option) 
   def editId(self, table, key, data): return self._editId(table, key, data) 
   def deleteBy(self, table, data): return self._deleteBy(table, data) 


#################################################################
######################## Sira Version 2.0.1 #####################
#################################################################
#-------------------------------------------
#-------------------------------------------
#db = mysqlDb()
#x = db.add("mpls_test_tb( type, des)", "('Test', 'Rachitha')" )
#print(x)

#-------------------------------------------
#-------------------------------------------
#db = mysqlDb()
#x = db.addList("mpls_test_tb( type, des)", " ('Test1', 'Rachitha'), ('Test2', 'Madusanka'), ('Test3', 'Gayan'), ('Test4', 'Sanjeewa') " )
#print(x)

#-------------------------------------------
#-------------------------------------------
#db = mysqlDb()
#result = db.view("mpls_test_tb", "id=42 OR id=43")
#for x in result[1]:
#    print(x)

#-------------------------------------------
#-------------------------------------------
#db = mysqlDb()
#result = db.editId("mpls_test_tb", "des=%s WHERE id=%s",  [("stig" , 39), ("ffig_hjgfjfgh" , 44),("ig" , 46)])
#print(result)

#-------------------------------------------
#-------------------------------------------
#db = mysqlDb()
#result = db.edit("mpls_test_tb", "des='trdtinhfghdfg'", " id=39 ")
#print(result)

#-------------------------------------------
#-------------------------------------------
#################################################################
