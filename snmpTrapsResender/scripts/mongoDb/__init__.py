#################################################################
######################## Sira Version 2.0.1 #####################
#################################################################

from pymongo import MongoClient
from bson.objectid import ObjectId

class __database:
    def __init__(self, dname="snmpTraps", Cport=27017):
        self.client = MongoClient(port=Cport)
        self.db_name = dname
        self.conn = self.client[self.db_name]
    ##########################
    def _add(self, collection_name, data):
        try:
            RE = self.conn[collection_name].insert_one(data)
            return [1, 'INSERTING A NEW RECORD TO MONGO DATABASE SUCCESSFULLY (_add->RE.inserted_id)', RE ]
        except Exception as error:
            return [0, 'FAILED INSERTING A NEW RECORD TO MONGO DATABASE (_add)', format(error)]
    ##########################
    def _addList(self, collection_name, data):
        try:
            RE = self.conn[collection_name].insert_many(data)
            return [1, 'INSERTING NEW RECORDS TO MONGO DATABASE SUCCESSFULLY (_addList->RE.inserted_ids)', RE ]
        except Exception as error:
            return [0, 'FAILED INSERTING NEW RECORDS TO MONGO DATABASE (_addList)', format(error)]
    ##########################
    def _view(self, collection_name, data):
        try:
            RE = self.conn[collection_name].find(data)
            return [1, 'VIEWING RECORDS IN MONGO DATABASE SUCCESSFULLY (_view)', RE ]
        except Exception as error:
            return [0, 'FAILED VIEWING RECORDS IN MONGO DATABASE (_view)', format(error)]
    ##########################
    def _viewSortLimit(self, collection_name, data, order, number):
        try:
            RE = self.conn[collection_name].find(data).sort(order).limit(number)
            return [1, 'VIEWING SORT RECORDS BY LIMIT IN MONGO DATABASE SUCCESSFULLY (_viewSortLimit)', RE ]
        except Exception as error:
            return [0, 'FAILED VIEWING SORT RECORDS BY LIMIT IN MONGO DATABASE (_viewSortLimit)', format(error)]
    ##########################
    def _edit(self, collection_name, data, key):
        try:
            RE = self.conn[collection_name].update_many(key, data)
            return [1, 'EDITING RECORDS IN MONGO DATABASE SUCCESSFULLY (_edit)', RE ]
        except Exception as error:
            return [0, 'FAILED EDITING RECORDS IN MONGO DATABASE (_edit)', format(error)]
    ##########################
    def _editId(self, collection_name, data, oid):
        try:
            RE = self.conn[collection_name].update_one(oid, data)
            return [1, 'EDITING RECORD BY ID IN MONGO DATABASE SUCCESSFULLY (_editId)', RE ]
        except Exception as error:
            return [0, 'FAILED EDITING RECORD BY ID IN MONGO DATABASE (_editId)', format(error)]
    ##########################
    def _deleteBy(self, collection_name, data):
        try:
            RE = self.conn[collection_name].delete_many(data)
            return [1, 'DELETE RECORD IN MONGO DATABASE SUCCESSFULLY (_deleteBy->RE.deleted_count)', RE ]
        except Exception as error:
            return [0, 'FAILED DELETE RECORD IN MONGO DATABASE (_deleteBy)', format(error)]

class mongoDb(__database):
   def add(self, collection, data): return self._add(collection, data) 
   def addList(self, collection, data): return self._addList(collection, data) 
   def view(self, collection, data): return self._view(collection, data) 
   def viewSortLimit(self, collection, data, order, number): return self._viewSortLimit(collection, data, order, number) 
   def edit(self, collection, data, key): return self._edit(collection, data, key) 
   def editId(self, collection, data, oid): return self._editId(collection, data, oid) 
   def deleteBy(self, collection, data): return self._deleteBy(collection, data) 



#################################################################
######################## Sira Version 2.0.1 #####################
#################################################################
#-------------------------------------------
#-------------------------------------------
#db = mongoDb("mpls", "pe")
#oid = {'_id': ObjectId('5db96364b395dd5412871b38')}
#data = { "$set": { "name": "Rachitha", "address": "colombo" }}
#cursor = db.editId(data, oid)
#cursorX = db.view({})
#for document in cursorX[1]:
#          print(document)
#-------------------------------------------
#-------------------------------------------
#db = mongoDb("mpls", "pe")
#key = { "name": "Saman" }
#data = { "$set": { "name": "kkk" }}
#cursor = db.edit(data, key)
#print(cursor[1].modified_count)
#cursorX = db.view({})
#for document in cursorX[1]:
#          print(document)
#-------------------------------------------
#-------------------------------------------
#db = mongoDb("mpls", "pe")
#mydict = { "name": "John" }
#cursor = db.viewSortLimit(mydict, "name", 5)
#for document in cursor[1]:
#    print(document)
#-------------------------------------------
#-------------------------------------------
#db = mongodb("snmpTraps")
#mydict = { }
#cursor = db.view('sent', mydict)
#for document in cursor[2]:
#    print(document)
#-------------------------------------------
#-------------------------------------------
#db = mongoDb("mpls", "pe")
#mydict = { "name": "John" }
#x = db.add(mydict)
#print(x)
#-------------------------------------------
#-------------------------------------------
#db = mongoDb("mpls", "pe")
#mydict = [ { "name": "John", "address": "Highway 37" }, { "name": "John", "address": "Highway 37" }]  
#x = db.addlist(mydict)
#print(x)
#-------------------------------------------
#-------------------------------------------

#################################################################

   
