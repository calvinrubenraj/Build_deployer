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
		
	#def delete_query(self,proname):	