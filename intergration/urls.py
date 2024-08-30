from . import views
from django.urls import path
urlpatterns =[
    path('', views.index, name='index'), #this is the url to initiate the stk push
    path('stk_push_callback/', views.stk_push_callback, name='stk_push_callback'), #this is the url to handle the callback after the stk push

]