class People:
    def __init__(self,firstname,lastname, middlename, age,city,country,PhotoFiles,work,edu,adress,event,contact,link,Photo,Photolink):
        #self.year = year
        #self.day=day
        #self.month=month
        #self.birthdate = birthdate
        self.first_name=firstname
        self.last_name=lastname
        self.middlename=middlename
        self.age=age
        self.city=city
        self.country=country
        self.PhotoFiles=PhotoFiles
        self.work = work
        self.edu = edu
        self.adress = adress
        self.event = event
        self.contact=contact
        self.link=link
        self.Photo=Photo
        self.Photolink=Photolink

    def __iter__(self):
        return self.__dict__.iteritems()

