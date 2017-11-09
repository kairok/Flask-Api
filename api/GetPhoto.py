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
from lunaReg import Luna


luna=Luna()

dbConf = DBconf.ConfigClass()
#svphoto=SavePeople()

host=dbConf.host
port=dbConf.port
client =MongoClient(host)
collection = client.Info_data.people
# Подключение к GridFS
db = client.Info_data
fs = gridfs.GridFS(db)


class GetPhotoFromSite:
    def SavePhotoGridFS(self, image, namefile):
        if fs.exists(filename=namefile + ".jpg"):
            return
            # Записать объект-файл
        stored = fs.put(image, filename=namefile + ".jpg")


    def saveLuna(self,url, idp, namefile):
        i=0
        #name=name.replace('.','')
        spis=[]
        try:

                jpgfile = urllib2.urlopen(url)
                image = jpgfile.read()
                #with open('Image/' + namefile+'.jpg', 'wb') as output:  #'Image/'+
                #        output.write(image)
                #self.SavePhotoGridFS(image, namefile)
                #spis.append(namefile)
                i += 1
                #  Save Image to Luna
                ret = luna.postimage(image)
                try:
                    if ret[u'error_code'] == 4003:
                        return
                except:
                    pass
                # Link id photo to person id
                for ph in ret[u'faces']:
                    print 'Save photo : ' + str(ph[u'score'])
                    if ph[u'score'] >= 0.995:
                        idphoto = ph[u'id']
                        luna.linkImagetoPerson(idp, idphoto)

                #self.getimage(url, namefile)



        except:
            if sys.exc_info()[1].code==404:
                pass
            else:
                print ("VK.com error I/O error  GetPhoto" + sys.exc_info()[1].strerror + ' line err ' + str(
                    sys.exc_info()[2].tb_lineno) )

            ok=1
        return spis

    def saveLunaVK(self, urlspis, name, idp):
        i = 0
        name = name.replace('.', '')
        spis = []
        try:
            for url in urlspis:
                namefile = name + '_' + str(i)
                print namefile
                outfilename = 'Image/' + namefile + '.jpg'

                jpgfile = urllib2.urlopen(url)
                image = jpgfile.read()
                # with open('Image/' + namefile+'.jpg', 'wb') as output:  #'Image/'+
                #        output.write(image)
                self.SavePhotoGridFS(image, namefile)
                spis.append(namefile)
                i += 1
                #  Save Image to Luna
                ret = luna.postimage(image)
                try:
                    if ret[u'error_code'] == 4003:
                        continue
                except:
                    pass
                # Link id photo to person id
                for ph in ret[u'faces']:
                    print 'Save photo : ' + str(ph[u'score'])
                    if ph[u'score'] >= 0.995:
                        idphoto = ph[u'id']
                        luna.linkImagetoPerson(idp, idphoto)

                        # self.getimage(url, namefile)

                        # with open( 'Image/' +  namefile + '.jpg', 'wb') as output:  #'~/WorkPython/Socialnet/Image/' +
                        #    output.write(image)

        except:
            if sys.exc_info()[1].code == 404:
                pass
            else:
                print ("VK.com error I/O error  GetPhoto" + sys.exc_info()[1].strerror + ' line err ' + str(
                    sys.exc_info()[2].tb_lineno))

            ok = 1
        return spis

    def save(self,urlspis, name):
        i=0
        name=name.replace('.','')
        spis=[]
        try:
            for url in urlspis:
                namefile = name + '_'+str(i)
                print namefile
                outfilename = 'Image/' + namefile + '.jpg'

                jpgfile = urllib2.urlopen(url)
                image = jpgfile.read()
                # with open('Image/' + namefile+'.jpg', 'wb') as output:  #'Image/'+
                #        output.write(image)
                self.SavePhotoGridFS(image, namefile)
                #self.getimage(url, namefile)
                spis.append(namefile)


                #with open( 'Image/' +  namefile + '.jpg', 'wb') as output:  #'~/WorkPython/Socialnet/Image/' +
                #    output.write(image)
                i+=1
        except:
            if sys.exc_info()[1].code==404:
                pass
            else:
                print ("VK.com error I/O error  GetPhoto" + sys.exc_info()[1].strerror + ' line err ' + str(
                    sys.exc_info()[2].tb_lineno) )

            ok=1
        return spis

    def getphoto(self, contacts):
        spis=[]
        name=contacts['domain']
        try:
            url=contacts['photo_400_orig']
            namefile=name+'_photo_400'
            self.getimage(url,namefile)
            spis.append(namefile)

            url =contacts['photo_200_orig']
            namefile = name + '_photo_200'
            self.getimage(url, namefile)
            spis.append(namefile)

            #url =contacts['photo_50']
            #namefile = name + '_photo_50'
            #self.getimage(url, namefile)
            #spis.append(namefile)

            #url =contacts['photo_max']
            #namefile = name + '_photo_max'
            #self.getimage(url, namefile)
            #spis.append(namefile)

            url =contacts['photo_max_orig']
            namefile = name + '_photo_max'
            self.getimage(url, namefile)
            spis.append(namefile)

        except:
            pass
        return spis


    def getimage(self,url, namefile):
        try:
            outfilename = 'Image/' + namefile + '.jpg'

            jpgfile = urllib2.urlopen(url)
            image = jpgfile.read()
            #with open('Image/' + namefile+'.jpg', 'wb') as output:  #'Image/'+
            #        output.write(image)
            self.SavePhotoGridFS(image,namefile)
        except:
            if sys.exc_info()[1].code==404:
                pass
            else:
                print ("VK.com error I/O error  GetPhoto" + sys.exc_info()[1].strerror + ' line err ' + str(
                    sys.exc_info()[2].tb_lineno))

        '''
        if fs.exists(filename=namefile+".jpg"):
            return

        # Записать объект-файл
        stored = fs.put(image, filename=namefile+".jpg")
        '''
        #self.getphotoGridfs(stored,namefile)
        #self.getphotoByNameFile(namefile)


    def getphotoGridfsbyID(self,file_id, namefile):
        with open('Image/' + namefile + '.jpg', 'wb') as output:
            output.write(fs.get(file_id).read())
            ok=1

    def getphotoByNameFile(self, namefile):
        outputdata = fs.find_one({"filename": "grebennikov_v_photo_100.jpg"}).read()
        with open('Image/' + namefile + '.jpg', 'wb') as output:
            output.write(outputdata)

