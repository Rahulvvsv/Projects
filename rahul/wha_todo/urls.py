from django.urls import path
from wha_todo import views
app_name ='wha_todo'
urlpatterns = [

        path('',views.what1,name='todo'),
        # path('login/', views.login ,name='login'),
        path('register/',views.register,name='register'),
        path('index/',views.index,name='index'),
        path('user_login/',views.user_login,name='user_login'),
]
