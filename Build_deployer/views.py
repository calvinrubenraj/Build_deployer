from django.shortcuts import render
import json
from django.http import QueryDict

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from Build_deployer.bin.form.login_form import LoginForm

from Build_deployer.bin.validation.login import login_validation_class
from Build_deployer.bin.db.file_form_db import *
from Build_deployer.bin.data.plugindata import *




# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        form = LoginForm(request.GET)
        render(request, 'login.jsp', {'form': form})
        
def CygnetFileProfPageView(request):
    if request.method == 'GET':
        #Get the profile list from db
        dbconnection()
        cygprofadd=cyg_prof_db_query
        proflist=cygprofadd.get_prof_list_query(cygprofadd)
        #Change the format according to 
        pluginlistobj=pluginlist
        profarr=pluginlist.id_text_list(pluginlistobj,proflist)
#         for idx, val in enumerate(proflist):
#             profdir={}
#             profdir["id"]=str(idx+1)
#             profdir["text"]=val
#             profarr.append(profdir)
            
        #profdir = json.dumps(profdir)
        print(profarr)

        return render(request, 'CygFileProf.html', {'profarr' : profarr})
    
class M6FileProfPageView(TemplateView):
    template_name = "M6FileProf.html"
    
class M6EncrptyFileProfPageView(TemplateView):
    template_name = "M6EnctFileProf.html" 
    
def CygnetAddFileProfPageView(request):
    if request.method == 'GET':
        dbconnection()
        cygprofadd=cyg_prof_db_query
        proflist=cygprofadd.get_prof_list_query(cygprofadd)
        proflist = json.dumps(proflist)
        print(proflist)
        return render(request, 'CygAddFileProf.html', {'proflist': proflist}, )
       
  
class M6AddFileProfPageView(TemplateView):
    template_name = "M6AddFileProf.html"  
    
class M6EnctAddFileProfPageView(TemplateView):
    template_name = "M6EnctAddFileProf.html"    
    
class TemplatesView(TemplateView):
    template_name = "LeftNav.html"

class TestView(TemplateView):    
    template_name = "Dashboard.html"
    
class CompleteView(TemplateView):    
    template_name = "Complete.html"

def login_validation(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        print(form)
        login_valid_object=login_validation_class
        valid = login_valid_object.login_check(login_valid_object, form)
        if(valid):
            return render(request, 'Dashboard.html')
        return render(request, 'login.jsp', {'login_form': form, 'login_fail':''})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
        return render(request, 'login.jsp', {'login_form': form,'login_fail':'hidden'})
    
def cyg_add_prof_validation(request):
    if request.method == 'POST':
        #get form value to save in db
        cygaddvaldir=request.POST
        print(cygaddvaldir)
        dbconnection()
        cygprofadd=cyg_prof_db_query
        cygprofadd.insert_query(cygprofadd,cygaddvaldir)
        return render(request, 'Complete.html',{'result': "Cygnet profile added",'location':'/build/CygFileProf.html'})
        
def cyg_del_prof_validation(request):
    if request.method == 'POST':
        cygdelvaldir=request.POST
        idList = cygdelvaldir.getlist('cygdellist')
        #Get the profile list from db
        dbconnection()
        cygprofqueryobj=cyg_prof_db_query
        proflist=cygprofqueryobj.get_prof_list_query(cygprofqueryobj)
        #Change the format according to 
        pluginlistobj=pluginlist
        #print(myDict['cygdellist'])
        profnamearr=pluginlist.convert_id_text_list(pluginlistobj,proflist,idList)
        print(profnamearr)
        #delete the profile in profnamearr
        cygprofqueryobj.del_prof_query(cygprofqueryobj,profnamearr)
        print("profile deleted")
        return render(request, 'Complete.html',{'result': "Cygnet profile added",'location':'/build/CygFileProf.html'})
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        