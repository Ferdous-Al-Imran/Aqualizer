from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import User,ParameterList,ValueEntry,ParameterIdeals
from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView

# class SensorValueView(TemplateView):
#     context_object_name = 'sensorValue'    
#     template_name = "sensorValue/index.html"
#     queryset = User.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super(SensorValueView, self).get_context_data(**kwargs)
#         context['user'] = User.objects.all()
#         context['parameterList'] = ParameterList.objects.all()
#         context['valueEntry'] = ValueEntry.objects.all()
#         context['parameterIdeals'] = ParameterIdeals.objects.all()
#         # And so on for more models
#         return context

def SensorValueView(request,user_id):
    all_user = User.objects.get(id=user_id)
    parameter_list = ParameterList.objects.all()
    value_entry = ValueEntry.objects.all()
    parameter_ideals = ParameterIdeals.objects.filter(userId=user_id) 
    template=loader.get_template('sensorValue/index.html') 
    context = {
        'all_user':all_user,
        'parameter_list':parameter_list,
        'value_entry':value_entry,
        'parameter_ideals':parameter_ideals,
    }

    return HttpResponse(template.render(context,request))









