

import os
from lunaReg import Luna
import json




luna=Luna()


ret=luna.GetList()
idlist=ret[u'lists'][u'person_lists'][0][u'id']
ok=1

directory = '/home/kai/WorkPython/Restapi/Image/'
files = os.listdir(directory)
for f in files:
  ret=luna.SearchbyPhotoFileLists(directory+f, idlist)
  cand=json.loads(ret.content)
  for pers in cand[u'candidates']:
      if pers[u'similarity']>0.97:
          id=pers[u'descriptor_id']
          fio=pers[u'user_data']
          print fio

  ok=1

'''
#  Search by Photo from file
ret=luna.getperson()
idp=0
spispers=''
l=1
for i in ret[u'persons']:
   idp=i[u'id']
   fio=i[u'user_data']

   if l>2:
       spispers += idp
       #break
   else:
       spispers += idp + '%2C'
   l+=1
   if l>3:
       break


directory = '/home/kai/WorkPython/Restapi/Image/'
files = os.listdir(directory)
for f in files:
  ret=luna.SearchbyPhotoFile(directory+f, spispers)
  cand=json.loads(ret.content)
  for pers in cand[u'candidates']:
      if pers[u'similarity']>0.9:
          id=pers[u'descriptor_id']
          fio=pers[u'user_data']
          print fio

  ok=1
  
  
'''

print 'Done!'