from django.urls import path , include
from . import views
urlpatterns = [

path("",views.index_page,name="index_page")

]