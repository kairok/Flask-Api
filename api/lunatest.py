# -*- coding: utf-8 -*-

import os
from lunaReg import Luna
import requests
import json

luna=Luna()



#r = requests.get("http://luna2.1cb.kz:8080/1/storage/persons", auth=('kairat@1cb.kz', 'poi12345'))


#ret=luna.GetList()
#idlist=ret[u'lists'][u'person_lists'][0][u'id']
ok=1
#  Patch Lists to Person
#ret=luna.getperson()
r = requests.get("http://luna2.1cb.kz:8080/1/storage/persons?page=1&page_size=100", auth=('kairat@1cb.kz', 'poi12345'))
ret=json.loads(r.content)
idp=0
col=1
for i in ret[u'persons']:
   print str(col)
   idp=i[u'id']
   fio=i[u'user_data']
   print fio
   luna.deleteperson(idp)
   col+=1
   #if u'Сергей' in fio:
   #     luna.deleteperson(idp)
   #luna.PatchtoPersonLists(idp,idlist)


ok=1

'''
#Get images  and LinkToPerson
ret=luna.getperson()
idp=0
for i in ret[u'persons']:
   idp=i[u'id']
   fio=i[u'user_data']
   for photo in i[u'descriptors']:
       idphoto=photo
       ret=luna.GetPhoto(idphoto)
       ok=1
'''



# Create person
fio='Кайрат Койба'
#ret=luna.postperson(fio)


# Get person
ret=luna.getperson()
idp=0
for i in ret[u'persons']:
   idp=i[u'id']
   fio=i[u'user_data']
   if u'petia' in fio:
       #luna.deleteperson(idp)
       break
   #for phi in i[u'descriptors']:
   #  t=GetPhoto(phi)


# Post image to Luna from directory images

directory = '/home/kai/WorkPython/Restapi/Image'
files = os.listdir(directory)
for f in files:
  ret=luna.postimage(directory+f)
  try:
    if ret[u'error_code']==4003:
      continue
  except:
    pass
  # Link id photo to person id
  for ph in ret[u'faces']:
        print 'Save photo : '+str(ph[u'score'])
        if ph[u'score']>=0.995:
            idphoto=ph[u'id']
            luna.linkImagetoPerson(idp, idphoto)





'''
directory = '/home/kai/WorkPython/websocial/Image (copy)/'
files = os.listdir(directory)
for f in files:
  ret=postimage(directory+f)
  ok=1
  for ph in ret[u'faces']:
      idphoto=ph['id']
      score=ph[u'score']
      Search(idphoto)

'''






# Create List
#ret=CreateList()
#idlist=ret[u'list_id']

#Get List
#ret=GetList()

#StoreImagetoList
#ret=linkImagetoList(idlist,idphoto)


#Get images  and LinkToPerson
ret=luna.GetImage()
for i in ret[u'descriptors']:
  idphoto = i[u'id']
  luna.linkImagetoPerson(idp, idphoto)
  #linkImagetoList(idlist, idphoto)
  ok=1

# Linked List image to person id
#linkImagetoPerson()




# Find photo

ok=1

#
#
#getacc()
#gettoken()
#
