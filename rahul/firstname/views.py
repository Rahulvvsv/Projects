from django.shortcuts import render
from firstname.models import *
# Create your views here.

from firstname import forms

def index(request):
    form = forms.forms1()
    if request.method == "POST":
        form1 = forms.forms1(request.POST)
        if form1.is_valid():
            print(form1.cleaned_data['Name'])



    details = jose.objects.order_by("lastname")
    context={'helo':details,'form':form,}
    return render(request,"firstname/rahul.html",context)
