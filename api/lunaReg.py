# -*- coding: utf-8 -*-

import requests
import json
import os


class Luna:
  def createacc(self):
    form = {
      "organization_name": "1CB",
      "email": "kairat@1cb.kz",
      "password": "poi12345"
    }
    r = requests.post("http://luna2.1cb.kz:8080/1/accounts", data=json.dumps(form))
    #r = requests.post("http://www.cloudypoint.com/Tutorials/discussion/docker-solved-cant-download-python-packages-onto-docker-image/")
    ok=1


  def getacc(self):
    form = {
      "organization_name": "1CB",
      "email": "kairat@1cb.kz",
      "suspended": "false"
    }
    r = requests.post("http://luna2.1cb.kz:8080/1/account", data=json.dumps(form))
    #r = requests.post("http://www.cloudypoint.com/Tutorials/discussion/docker-solved-cant-download-python-packages-onto-docker-image/")
    ok=1


  def gettoken(self):
    r = requests.post("http://luna2.1cb.kz:8080/1/account/tokens")
    # r = requests.post("http://www.cloudypoint.com/Tutorials/discussion/docker-solved-cant-download-python-packages-onto-docker-image/")
    ok = 1

  def postperson(self,fio):
    form = {
    "user_data": fio
    }
    r = requests.post("http://luna2.1cb.kz:8080/1/storage/persons", auth=('kairat@1cb.kz', 'poi12345'), data=json.dumps(form))
    # r = requests.post("http://www.cloudypoint.com/Tutorials/discussion/docker-solved-cant-download-python-packages-onto-docker-image/")
    ok = 1
    res = json.loads(r.content)
    return res

  def getperson(self, page):
    sql = "http://luna2.1cb.kz:8080/1/storage/persons?page=%s&page_size=100" % page
    r = requests.get(sql, auth=('kairat@1cb.kz', 'poi12345'))
    # r = requests.post("http://www.cloudypoint.com/Tutorials/discussion/docker-solved-cant-download-python-packages-onto-docker-image/")
    res=json.loads(r.content)
    ok = 1
    return res

  def deleteperson(self, idp):
    sql="http://luna2.1cb.kz:8080/1/storage/persons/"+idp
    r = requests.delete(sql, auth=('kairat@1cb.kz', 'poi12345'))
    # r = requests.post("http://www.cloudypoint.com/Tutorials/discussion/docker-solved-cant-download-python-packages-onto-docker-image/")
    res=r.content
    ok = 1
    return res

  def postimage(self,jpgdata):
    #namefile='/home/kai/WorkPython/websocial/api/Image/id1719512611.jpg'

    headers = {'Content-type': 'image/jpeg'}
    r = requests.post("http://luna2.1cb.kz:8080/1/storage/descriptors", auth=('kairat@1cb.kz', 'poi12345'), headers=headers,data=jpgdata)
    # r = requests.post("http://www.cloudypoint.com/Tutorials/discussion/docker-solved-cant-download-python-packages-onto-docker-image/")
    ok = 1
    res = json.loads(r.content)
    ok = 1
    return res


  def postimagefile(self,namefile):
    #namefile='/home/kai/WorkPython/websocial/api/Image/id1719512611.jpg'

    f = open(namefile, 'r+')
    jpgdata = f.read()
    f.close()
    headers = {'Content-type': 'image/jpeg'}
    r = requests.post("http://luna2.1cb.kz:8080/1/storage/descriptors", auth=('kairat@1cb.kz', 'poi12345'), headers=headers,data=jpgdata)
    # r = requests.post("http://www.cloudypoint.com/Tutorials/discussion/docker-solved-cant-download-python-packages-onto-docker-image/")
    ok = 1
    res = json.loads(r.content)
    ok = 1
    return res

  def GetImage(self):
    form = {
      "user_data": "petia"
    }
    r = requests.get("http://luna2.1cb.kz:8080/1/storage/descriptors", auth=('kairat@1cb.kz', 'poi12345') )
    # r = requests.post("http://www.cloudypoint.com/Tutorials/discussion/docker-solved-cant-download-python-packages-onto-docker-image/")
    ok = 1
    res = json.loads(r.content)
    return res

  def linkImagetoPerson(self,idpers,idphoto):

    sql="http://luna2.1cb.kz:8080/1/storage/persons/%s/linked_descriptors?descriptor_id=%s&do=attach"%(idpers,idphoto)
    r = requests.patch(sql, auth=('kairat@1cb.kz', 'poi12345')) #, data=json.dumps(form)

    ok = 1
    print str(r.status_code)+'  '+idphoto
    #res = json.loads(r.content)
    return r


  def PatchtoPersonLists(self,idpers,idlist):

    sql="http://luna2.1cb.kz:8080/1/storage/persons/%s/linked_lists?list_id=%s&do=attach"%(idpers,idlist)
    r = requests.patch(sql, auth=('kairat@1cb.kz', 'poi12345')) #, data=json.dumps(form)

    ok = 1
    print str(r.status_code)+'  '+idlist
    #res = json.loads(r.content)
    return r



  def CreateList(self):
    form = {
      "list_data": "descriptors"
    }
    sql="http://luna2.1cb.kz:8080/1/storage/lists"
    r = requests.post(sql, auth=('kairat@1cb.kz', 'poi12345'), data=json.dumps(form))

    ok = 1
    res = json.loads(r.content)
    return res


  def GetList(self):

    sql="http://luna2.1cb.kz:8080/1/storage/lists"
    r = requests.get(sql, auth=('kairat@1cb.kz', 'poi12345'))

    ok = 1
    res = json.loads(r.content)
    return res


  def linkImagetoList(self,idlist,idphoto):
    form = {
      "list_id": idphoto
    }
    sql="http://luna2.1cb.kz:8080/1/storage/descriptors/{%s}/linked_lists"%idlist
    r = requests.post(sql, auth=('kairat@1cb.kz', 'poi12345'), data=json.dumps(form))

    ok = 1
    res = json.loads(r.content)
    return res


  def GetPhoto(self,idphoto):
    headers = {'Content-type': 'image/jpeg'}
    sql="http://luna2.1cb.kz:8080/1/storage/portraits/%s"%idphoto
    r = requests.get(sql, auth=('kairat@1cb.kz', 'poi12345'), headers=headers) #, data=json.dumps(form)

    ok = 1
    print str(r.status_code)+'  '+idphoto
    #res = json.loads(r.content)
    return r



  def Search(self,idphoto):
    headers = {'Content-type': 'image/jpeg'}
    sql="http://luna2.1cb.kz:8080/1/matching/verify?descriptor_id=%s"%idphoto
    r = requests.post(sql, auth=('kairat@1cb.kz', 'poi12345'), headers=headers)

    ok = 1
    print str(r.status_code)+'  '+idphoto
    #res = json.loads(r.content)
    return r


  def SearchbyPhotoFile(self,namefile, persons):
    f = open(namefile, 'r+')
    jpgdata = f.read()
    f.close()
    headers = {'Content-type': 'image/jpeg'}

    sql="http://luna2.1cb.kz:8080/1/matching/search?person_ids=%s"%persons
    r = requests.post(sql, auth=('kairat@1cb.kz', 'poi12345'), headers=headers, data=jpgdata)

    ok = 1
    print str(r.status_code)+'  '+namefile
    #res = json.loads(r.content)
    return r

  def SearchbyPhotoFileLists(self,namefile, idlist):
    f = open(namefile, 'r+')
    jpgdata = f.read()
    f.close()
    headers = {'Content-type': 'image/jpeg'}

    sql="http://luna2.1cb.kz:8080/1/matching/search?list_id=%s"%idlist
    r = requests.post(sql, auth=('kairat@1cb.kz', 'poi12345'), headers=headers, data=jpgdata)

    ok = 1
    print str(r.status_code)+'  '+namefile
    #res = json.loads(r.content)
    return r

  def SearchbyPhoto(self,image, persons):

    headers = {'Content-type': 'image/jpeg'}

    sql="http://luna2.1cb.kz:8080/1/matching/search?person_ids=%s"%persons
    r = requests.post(sql, auth=('kairat@1cb.kz', 'poi12345'), headers=headers, data=image)

    ok = 1
    print str(r.status_code)
    #res = json.loads(r.content)
    return r

  def SearchbyPhotoLists(self,image, idlist):

    headers = {'Content-type': 'image/jpeg'}

    sql="http://luna2.1cb.kz:8080/1/matching/search?list_id=%s"%idlist
    r = requests.post(sql, auth=('kairat@1cb.kz', 'poi12345'), headers=headers, data=image)

    ok = 1
    print 'Find from Lists '+str(r.status_code)+'  '+idlist
    #res = json.loads(r.content)
    return r

#--------------------------------------------------------------------------------
# Test Search
