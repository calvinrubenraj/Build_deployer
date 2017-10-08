from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from Build_deployer.bin.form.login_form import LoginForm

from Build_deployer.bin.validation.login import login_validation_class
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        form = LoginForm(request.GET)
        render(request, 'login.jsp', {'form': form})
        
class CygnetFileProfPageView(TemplateView):
    template_name = "CygFileProf.html"
    
class M6FileProfPageView(TemplateView):
    template_name = "M6FileProf.html"
    
class M6EncrptyFileProfPageView(TemplateView):
    template_name = "M6EnctFileProf.html" 
    
class CygnetAddFileProfPageView(TemplateView):
    template_name = "CygAddFileProf.html"   
    
class TemplatesView(TemplateView):
    template_name = "LeftNav.html"

class TestView(TemplateView):    
    template_name = "Dashboard.html"

def login_validation(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        login_valid_object=login_validation_class
        valid = login_valid_object.login_check(login_valid_object, form)
        if(valid):
            return render(request, 'Dashboard.html')
        return render(request, 'login.jsp', {'login_form': form, 'login_fail':''})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
        return render(request, 'login.jsp', {'login_form': form,'login_fail':'hidden'})
