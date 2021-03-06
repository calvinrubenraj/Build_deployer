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
        
def CygnetFileProfPageView(request):
    if request.method == 'GET':
        #Get the profile list from db
        dbconnection()
        cygproflist=cyg_prof_db_query
        proflist=cygproflist.get_prof_list_query(cygproflist)
        #Change the format according to 
        pluginlistobj=pluginlist
        profarr=pluginlist.id_text_list(pluginlistobj,proflist)
        print(profarr)

        return render(request, 'CygFileProf.html', {'profarr' : profarr})
    
def CygnetAddFileProfPageView(request):
    if request.method == 'GET':
        dbconnection()
        cygproflist=cyg_prof_db_query
        proflist=cygproflist.get_prof_list_query(cygproflist)
        proflist = json.dumps(proflist)
        print(proflist)
        return render(request, 'CygAddFileProf.html', {'proflist': proflist}, )
    
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
        return render(request, 'Complete.html',{'result': "Cygnet profile deleted",'location':'/build/CygFileProf.html'})
    
def M6FileProfPageView(request):
    if request.method == 'GET':
        #Get the profile list from db
        dbconnection()
        m6proflist=m6_prof_db_query
        proflist=m6proflist.get_prof_list_query(m6proflist)
        #Change the format according to 
        pluginlistobj=pluginlist
        profarr=pluginlist.id_text_list(pluginlistobj,proflist)
        print(profarr)

        return render(request, 'M6FileProf.html', {'profarr' : profarr})

def M6AddFileProfPageView(request):
    if request.method == 'GET':
        dbconnection()
        m6proflist=m6_prof_db_query
        proflist=m6proflist.get_prof_list_query(m6proflist)
        proflist = json.dumps(proflist)
        print(proflist)
        return render(request, 'M6AddFileProf.html', {'proflist': proflist}, )
    
def m6_add_prof_validation(request):
    if request.method == 'POST':
        #get form value to save in db
        m6addvaldir=request.POST
        print(m6addvaldir)
        dbconnection()
        m6profadd=m6_prof_db_query
        m6profadd.insert_query(m6profadd,m6addvaldir)
        return render(request, 'Complete.html',{'result': "M6 profile added",'location':'/build/M6FileProf.html'})
        
def m6_del_prof_validation(request):
    if request.method == 'POST':
        m6delvaldir=request.POST
        idList = m6delvaldir.getlist('m6dellist')
        #Get the profile list from db
        dbconnection()
        m6profqueryobj=m6_prof_db_query
        proflist=m6profqueryobj.get_prof_list_query(m6profqueryobj)
        #Change the format according to 
        pluginlistobj=pluginlist
        #print(myDict['cygdellist'])
        profnamearr=pluginlist.convert_id_text_list(pluginlistobj,proflist,idList)
        print(profnamearr)
        #delete the profile in profnamearr
        m6profqueryobj.del_prof_query(m6profqueryobj,profnamearr)
        print("profile deleted")
        return render(request, 'Complete.html',{'result': "M6 profile deleted",'location':'/build/M6FileProf.html'})    

    
def M6EncrptyFileProfPageView(request):
    if request.method == 'GET':
        #Get the profile list from db
        dbconnection()
        m6enctproflist=m6enct_prof_db_query
        proflist=m6enctproflist.get_prof_list_query(m6enctproflist)
        #Change the format according to 
        pluginlistobj=pluginlist
        profarr=pluginlist.id_text_list(pluginlistobj,proflist)
            
        print(profarr)

        return render(request, 'M6EnctFileProf.html', {'profarr' : profarr})
   
def M6EnctAddFileProfPageView(request):
    if request.method == 'GET':
        dbconnection()
        m6enctproflist=m6enct_prof_db_query
        proflist=m6enctproflist.get_prof_list_query(m6enctproflist)
        proflist = json.dumps(proflist)
        print(proflist)
        return render(request, 'M6EnctAddFileProf.html', {'proflist': proflist}, )
    
def m6enct_add_prof_validation(request):
    if request.method == 'POST':
        m6enctaddvaldir=request.POST
        print(m6enctaddvaldir)
        dbconnection()
        m6enctprofadd=m6enct_prof_db_query
        m6enctprofadd.insert_query(m6enctprofadd,m6enctaddvaldir)
        return render(request, 'Complete.html',{'result': "M6 Encrypt file profile added",'location':'/build/M6EnctFileProf.html'})

def m6enct_del_prof_validation(request):
    if request.method == 'POST':
        m6delvaldir=request.POST
        idList = m6delvaldir.getlist('m6enctdellist')
        #Get the profile list from db
        dbconnection()
        m6enctprofqueryobj=m6enct_prof_db_query
        proflist=m6enctprofqueryobj.get_prof_list_query(m6enctprofqueryobj)
        #Change the format according to 
        pluginlistobj=pluginlist
        #print(myDict['cygdellist'])
        profnamearr=pluginlist.convert_id_text_list(pluginlistobj,proflist,idList)
        print(profnamearr)
        #delete the profile in profnamearr
        m6enctprofqueryobj.del_prof_query(m6enctprofqueryobj,profnamearr)
        print("profile deleted")
        return render(request, 'Complete.html',{'result': "M6 Encrypt file profile deleted",'location':'/build/M6EnctFileProf.html'})

def SshProfPageView(request):
    if request.method == 'GET':
        #Get the profile list from db
        dbconnection()
        sshproflist=ssh_prof_db_query
        proflist=sshproflist.get_prof_list_query(sshproflist)
        #Change the format according to 
        pluginlistobj=pluginlist
        profarr=pluginlist.id_text_list(pluginlistobj,proflist)
        print(profarr)

        return render(request, 'SshProf.html', {'profarr' : profarr})

def SshAddProfPageView(request):
    if request.method == 'GET':
        dbconnection()
        sshproflist=ssh_prof_db_query
        proflist=sshproflist.get_prof_list_query(sshproflist)
        proflist = json.dumps(proflist)
        print(proflist)
        return render(request, 'SshAddProf.html', {'proflist': proflist}, )
    
def ssh_add_prof_validation(request):
    if request.method == 'POST':
        sshaddvaldir=request.POST
        print(sshaddvaldir)
        dbconnection()
        sshprofadd=ssh_prof_db_query
        sshprofadd.insert_query(sshprofadd,sshaddvaldir)
        return render(request, 'Complete.html',{'result': "SSH profile added",'location':'/build/SshProf.html'})

def ssh_del_prof_validation(request):
    if request.method == 'POST':
        sshdelvaldir=request.POST
        idList = sshdelvaldir.getlist('sshdellist')
        #Get the profile list from db
        dbconnection()
        sshprofqueryobj=ssh_prof_db_query
        proflist=sshprofqueryobj.get_prof_list_query(sshprofqueryobj)
        #Change the format according to 
        pluginlistobj=pluginlist
        #print(myDict['cygdellist'])
        profnamearr=pluginlist.convert_id_text_list(pluginlistobj,proflist,idList)
        print(profnamearr)
        #delete the profile in profnamearr
        sshprofqueryobj.del_prof_query(sshprofqueryobj,profnamearr)
        print("profile deleted")
        return render(request, 'Complete.html',{'result': "SSH profile deleted",'location':'/build/SshProf.html'})
    
def BuildDeploymentView(request):
    if request.method == 'GET':
        #Get the profile list from db
        dbconnection()
        sshproflist=ssh_prof_db_query
        proflist=sshproflist.get_prof_list_query(sshproflist)
        #Change the format according to 
        pluginlistobj=pluginlist
        sshprofarr=pluginlist.id_text_list(pluginlistobj,proflist)
        
        cygproflist=cyg_prof_db_query
        proflist=cygproflist.get_prof_list_query(cygproflist)
        #Change the format according to 
        pluginlistobj=pluginlist
        cygprofarr=pluginlist.id_text_list(pluginlistobj,proflist)
        
        m6proflist=m6_prof_db_query
        proflist=m6proflist.get_prof_list_query(m6proflist)
        #Change the format according to 
        pluginlistobj=pluginlist
        m6profarr=pluginlist.id_text_list(pluginlistobj,proflist)
        
        m6enctproflist=m6enct_prof_db_query
        proflist=m6enctproflist.get_prof_list_query(m6enctproflist)
        #Change the format according to 
        pluginlistobj=pluginlist
        m6enctprofarr=pluginlist.id_text_list(pluginlistobj,proflist)
        
        return render(request, 'BuildDeploy.html', {'sshprofarr': sshprofarr, 'cygprofarr' :cygprofarr,'m6profarr':m6profarr,'m6enctprofarr':m6enctprofarr})
        
class TemplatesView(TemplateView):
    template_name = "LeftNav.html"

class TestView(TemplateView):    
    template_name = "Dashboard.html"
    
class CompleteView(TemplateView):    
    template_name = "Complete.html"


   
        

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        