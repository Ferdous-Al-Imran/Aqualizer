from django.conf.urls import patterns,include,url
from . import views
app_name='userAuthentication'

urlpatterns = [
    url(r'^login/',views.LoginView.as_view(),name='login'),
    url(r'^register/',views.RegisterView.as_view(),name='register'),
]