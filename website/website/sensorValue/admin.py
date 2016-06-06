from django.contrib import admin
from .models import User,ParameterList,ValueEntry,ParameterIdeals

admin.site.register(User)
admin.site.register(ParameterList)
admin.site.register(ValueEntry)
admin.site.register(ParameterIdeals)
