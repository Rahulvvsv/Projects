from rest_frame import views
from django.urls import path
urlpatterns = [
    path('',views.index,name="index"),
    path('api',views.article_list,name="api"),
    path("api/<int:pk>/",views.article_id,name="api_id")
    
]
