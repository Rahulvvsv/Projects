from django.urls import path
from firstname import views

urlpatterns = [
                path('',views.index,name= "hello")


]
