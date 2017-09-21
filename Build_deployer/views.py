from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from Build_deployer.form.login_form import LoginForm
# Create your views here.
class HomePageView(TemplateView):
    """def get(self, request, **kwargs):
        return render(request, 'login.jsp', context=None)"""
    def get(self, request, **kwargs):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = LoginForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')
    
        # if a GET (or any other method) we'll create a blank form
        else:
            form = LoginForm()
    
        return render(request, 'login.jsp', {'form': form})
    
class AboutPageView(TemplateView):
    """def get(self, request, **kwargs):
        return render(request, 'about.html', context=None)"""
    template_name = "about.html"
    
class LoginFailedPageView(TemplateView):
    template_name = "login_failed.jsp"