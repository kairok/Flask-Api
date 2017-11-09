# -*- coding: utf-8 -*-


from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from api.VKsearch2 import VKsearch
from api.translit import  latinizator
import webbrowser as wb
from api.lunaReg import Luna
import json
import requests

from pymongo import MongoClient
from Configbase import DBconf



dbConf = DBconf.ConfigClass()

host=dbConf.host
port=dbConf.port
client =MongoClient(host)
collection = client.Info_data.conference


luna=Luna()

vk_find = VKsearch()

app = FlaskAPI(__name__)


idPerson=[]
idDomain=[]


@app.route("/storage/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail():
    """
    Retrieve, update or delete note instances.
    """

    if request.method == 'PUT':
        fio = request.data.get('fio', '')
        bdat= str(request.data.get('iin', ''))
        try:
            year='19'+bdat[:2]
            month=bdat[2:4]
            day=bdat[4:6]
            birth=day+'.'+month+'.'+year
        except:
            return {'text':'Birth Date Not Found! '+fio,'found':0}

        print 'Get request STORAGE '+fio
        postFacebook(fio)
        ret=1
        
        if bdat in 'None':
            return {'text': fio, 'found': ret}

        ret, listuser = vk_find.main(fio, birth)
        if ret == 'Not found!':
            print(latinizator(fio))
            Chel = latinizator(fio)
            ret, listuser = vk_find.main(Chel, birth)
            if listuser == '':
                if u'баев' in fio:
                    fam = fio.replace(u'ае', u'аые')
                    
                    Chel = latinizator(fam)
                    ret, listuser = vk_find.main(Chel, birth)
            ok = 1
        return {'text':fio,'found':ret}


    return ''




@app.route("/find2/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail2():
    """
    Retrieve, update or delete note instances.
    """
    who=[]
    if request.method == 'PUT':
        ok = 1
        img=request.data["data"].decode("base64")
        namefile='kai'
        
        print 'Get request!'
       
        idlist=u'dfe662aa-9cd2-45b2-a68d-156496342649'
        # Find person lists
        ret = luna.SearchbyPhotoLists(img, idlist)
        cand = json.loads(ret.content)
        id=0
        for pers in cand[u'candidates']:
            if pers[u'similarity'] > 0.95:
                id = pers[u'person_id']
                fio = pers[u'user_data']
                print fio+'  '+str(pers[u'similarity'])
                if id in idPerson:
                    id=-1
                else:
                    idPerson.append(id)
                #  Find in MongoDb

        if id ==0:
            print 'Not Found Person!!'
        else:
            if id>0:
                id=[]
                for post in collection.find({"id_person_luna":  { "$in" : idPerson}}):

                    ok=1
                    #id = post[u'id']
                    try:
                        idk=post[u'id']
                        who.append(post['first_name'])
                        print 'VK '+str(idk)
                        domain = post[u'domain']
                        url = 'https://vk.com/' + domain
                        if idk not in idDomain:
                            id.append('vk:'+str(idk))
                            idDomain.append(idk)
                            #break
                    except:
                        #pass
                        #url=post[u'link']
                        domain=post[u'domain']
                        who.append(post['first_name'])
                        print 'Facebook '+domain
                        if domain not in idDomain:
                            id.append('fc:'+domain)
                            idDomain.append(domain)

                if len(id)==0:
                    id=-1

          
            wb.get('firefox').open('http://localhost:5001/170138372/concreate/', new=0)
        return {'text':who,'found':id}

   
    return ''



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002,debug=True)



