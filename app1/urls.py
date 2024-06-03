from django.urls import path

from .views import create,getdata,update,delete

app_name='app1'

urlpatterns = [
    path('getdata/',getdata,name='getdata'),
    path('create/',create,name='create'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
]
