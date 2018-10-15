from django.urls import path
from dataterminal import views

urlpatterns=[
    path('',views.index, name='index')

]