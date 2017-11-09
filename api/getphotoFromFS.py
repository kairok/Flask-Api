

# -*- coding: utf-8 -*-

import os
import urllib2
from pymongo import MongoClient
from Configbase import DBconf
#from SavePeople import SavePeople
import sys
import gridfs
from gridfs import GridFSBucket
#from logtrap import loggingBase

dbConf = DBconf.ConfigClass()
#svphoto=SavePeople()

host=dbConf.host
port=dbConf.port
client =MongoClient(host)
collection = client.Info_data.people

db = client.Info_data
fs = gridfs.GridFS(db)





def getphotoByNameFile( file_id,namefile):
    outputdata = fs.find_one({"filename":file_id+ ".jpg"}).read()
    with open('Image/' + namefile + '.jpg', 'wb') as output:
        output.write(outputdata)




file_id='umutbek.alima_photo_max'
namefile='0'


getphotoByNameFile( file_id,namefile)
