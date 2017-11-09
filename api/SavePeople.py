#!/usr/bin/python
# -*- coding: utf-8 -*-



from pymongo import MongoClient
from Configbase import DBconf
import gridfs
import datetime

dbConf = DBconf.ConfigClass()

host=dbConf.host
port=dbConf.port
client =MongoClient(host)
collection = client.Info_data.conference
friends = client.Info_data.friends
posts = client.Info_data.posts

collection_info = client.big_data.Subject

# Подключение к GridFS
db = client.Info_data
fs = gridfs.GridFS(db)

class  SavePeople:

    def findManVK(self, idUser):
        f = collection.find({"domain": idUser}).count()

        return f

    def findManFC(self, idUser):

        f = collection.find({"link": idUser}).count()

        return f

    def saveComment(self,comment, idk,post_id):
        print 'Save Posts ---------- '
        ok=1

        self.deleteposts(idk,post_id)
        comment['crawled'] = datetime.datetime.now().strftime("%d-%m-%Y")
        comment['id_user'] = idk
        comment['post_id'] = post_id
        comment['Site'] = 'vk'
        posts.save(comment)



    def deleteposts(self,id_user,post_id):
        posts.remove({"id_user": id_user, "post_id": post_id})

    def savefriends(self, spis, idk):
        print 'Save  Friends ---------- '
        #for user in spis:
        #    self.deletefriend(user['id'], idk)
        ok=1
        for user in spis:
            user['crawled'] = datetime.datetime.now().strftime("%d-%m-%Y")
            user['id_link'] = idk
            user['Site'] = 'vk'
            self.deletefriend(user['id'],idk)
            friends.save(user)

    def deletefriend(self, idk, link):
        friends.remove({"id":idk, "id_link":link})  #

    def save(self, userd):
        f = collection.find({"domain": userd["domain"]}).count()
        if f>0:
            collection.remove({"domain": userd["domain"]})
        collection.save(userd)

    def findMan(self,idUser, date):
        if date in '':
            f = collection.find({"domain": idUser}).count()
        else:
            f=collection.find({ "domain" : idUser, "crawled":date }).count()
        return f

    def SavePhotoGridFS(self, image, namefile):
        if fs.exists(filename=namefile + ".jpg"):
            return
            # Записать объект-файл
        stored = fs.put(image, filename=namefile + ".jpg")

    def SavePost(self, post):
        post['view'] = 1
        collection_info.save(post)