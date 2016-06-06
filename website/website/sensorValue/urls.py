from django.conf.urls import patterns,include,url
from . import views
app_name='sensorValue'

urlpatterns = [
    url(r'^([0-9]+)/$',views.SensorValueView,name='sensorValue'),
   
]