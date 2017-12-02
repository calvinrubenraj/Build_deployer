from mongoengine import *
#Mongo db connection
class dbconnection():
    def __init__(self):
        connect('testbuild')

class cygnet_prof_coll(Document):
    cygprfname = StringField(max_length=255, required=True, primary_key=True)
    cygip = StringField(max_length=255)
    cygport = StringField(max_length=255)
    cygsid = StringField(max_length=255)
    cygurl = StringField(max_length=1024)
    cygusername = StringField(max_length=255, required=True)
    cygpassword = StringField(max_length=255, required=True)
    

