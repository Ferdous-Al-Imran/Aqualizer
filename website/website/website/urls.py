from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^sensorValue/', include(sensorValue.urls)),
    url(r'^home/',include('home.urls')),
    url(r'^userAuthentication/',include('userAuthentication.urls')),
    url(r'^sensorValue/',include('sensorValue.urls')),
]
