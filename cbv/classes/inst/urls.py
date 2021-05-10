from django.urls import path
from inst import views


app_name = 'inst'

urlpatterns = [
            path('list/',views.SchoolListView.as_view(),name= 'list'),
            path('',views.advcbv.as_view(),name= 'index'),
            path('list/<int:pk>/',views.SchoolDetailView.as_view(),name= 'index_pk')



]
