from django.conf.urls import patterns,include,url
from . import views
app_name='home'

urlpatterns = [
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
   
]