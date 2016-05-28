from django.shortcuts import render
from django.views.generic import TemplateView


class SensorValueView(TemplateView):
    template_name = "sensorValue/index.html"
