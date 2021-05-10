from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from inst import models
# Create your views here.



class advcbv(TemplateView):

    template_name = 'inst/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['inserthere'] = "hello there"
        return context



class SchoolListView(ListView):

    context_object_name = 'schools'
    model = models.school
    template_name= "inst/landing.html"


class SchoolDetailView(DetailView):


    context_object_name = 'school_detail'

    model = models.school

    template_name= "inst/detail.html"
