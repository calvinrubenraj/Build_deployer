'''
Created on Dec 5, 2017

@author: calvin
'''
class pluginlist():
    def id_text_list(self,proflist):
        retarr=[]
        for idx, val in enumerate(proflist):
            profdir={}
            profdir["id"]=str(idx+1)
            profdir["text"]=val
            retarr.append(profdir)
        return retarr
    def convert_id_text_list(self,proflist,idlist):
        id_text_list = self.id_text_list(self,proflist)
        #print(id_text_list)
        retarr=[]
        for id_irr in idlist:
            for id_text_val in id_text_list:
                if(id_text_val['id']==id_irr):
                    retarr.append(id_text_val['text'])
                    break
        return retarr
        