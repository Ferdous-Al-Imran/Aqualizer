from django.conf.urls import patterns,include,url
from . import views
app_name='sensorValue'

urlpatterns = [
    url(r'^$',views.SensorValueView.as_view(),name='sensorValue'),
   
]