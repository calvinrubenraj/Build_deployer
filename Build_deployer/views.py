from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login.html', context=None)
    
class AboutPageView(TemplateView):
    """def get(self, request, **kwargs):
        return render(request, 'about.html', context=None)"""
    template_name = "about.html"