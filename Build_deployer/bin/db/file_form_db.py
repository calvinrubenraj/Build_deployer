from Build_deployer.bin.db.db_connection import *

class cyg_prof_db_query():
# 	def _init(self):
# 		dbconnection()
	
	def insert_query(self,insert_dict):
		if(insert_dict.__contains__('cygurl')):
			insertquery = cygnet_prof_coll(cygprfname=insert_dict['cygprfname'], cygurl=insert_dict['cygurl'], cygusername=insert_dict['cygusername'], cygpassword=insert_dict['cygpassword'])
		else:
			insertquery = cygnet_prof_coll(cygprfname=insert_dict['cygprfname'], cygip=insert_dict['cygip'], cygport=insert_dict['cygport'], cygsid=insert_dict['cygsid'], cygusername=insert_dict['cygusername'], cygpassword=insert_dict['cygpassword'])
		insertquery.save()
		
	def get_prof_list_query(self):
		ret_list_prof=[]
		for profi in cygnet_prof_coll.objects:
			ret_list_prof.append(profi.cygprfname)
		return ret_list_prof
	
	def del_prof_query(self,prof_list):
		for prof in prof_list:
			profobj = cygnet_prof_coll.objects(cygprfname=prof)
			profobj.delete()
		
	#def delete_query(self,proname):	
	
class m6_prof_db_query():
	
	def insert_query(self,insert_dict):
		if(insert_dict.__contains__('m6url')):
			insertquery = m6_prof_coll(m6prfname=insert_dict['m6prfname'], cygurl=insert_dict['m6url'], cygusername=insert_dict['m6username'], cygpassword=insert_dict['m6password'])
		else:
			insertquery = m6_prof_coll(m6prfname=insert_dict['m6prfname'], m6ip=insert_dict['m6ip'], m6port=insert_dict['m6port'], m6sid=insert_dict['m6sid'], m6username=insert_dict['m6username'], m6password=insert_dict['m6password'])
		insertquery.save()
		
	def get_prof_list_query(self):
		ret_list_prof=[]
		for profi in m6_prof_coll.objects:
			ret_list_prof.append(profi.m6prfname)
		return ret_list_prof
	
	def del_prof_query(self,prof_list):
		for prof in prof_list:
			profobj = m6_prof_coll.objects(m6prfname=prof)
			profobj.delete()