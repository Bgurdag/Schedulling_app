from django.urls import path

from . views import homepage
#Creates homepage and access to it
app_name = "schedulling"

urlpatterns = [
    path('', homepage, name="home"),
    #path('form', submit_event, name= "submitevent"),
] 


