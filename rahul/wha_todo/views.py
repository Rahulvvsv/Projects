from django.shortcuts import render,redirect
from wha_todo.forms import *
from wha_todo.models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def what1(request):
    work1 = work.objects.all()
    # work1 = work.objects.order_by("todo")
    form = lists()
    if request.method =="POST":
        form=lists(request.POST)
        if form.is_valid():
            form.save()
        return redirect(".")
    context = {'forms':form,"tasks":work1}
    return render(request,"wha_todo/todo.html",context)




def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserForm1(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserForm1()
    context ={'user_form':user_form,"profile_form":profile_form,'registered':registered}

    return render(request,'wha_todo/registration.html',context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('wha_todo:index'))



def index(request):
    return render(request,'wha_todo/index.html',context={})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')


        user = authenticate(username= username , password = password )


        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('wha_todo:index'))

            else:
                return HttpResponse("Accont not active")

        else:
            print("someone tried to login and failed ")
            print(f"Username :{username} and password :{password}")
            return HttpResponse("Invalid login credentials")



    else:
        return render(request,'wha_todo/login.html',context={})
