from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View 
from .forms import UserForm
from .models import UserInfo

class HomeView(TemplateView):
    template_name = "home/home.html"



class UserFormView(View):
	form_class=UserForm
	template_name='home/registration_form.html'

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)

			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()


			# returns User object if credentials are correct
			if user is not None:


				if user.is_active:
					login(request,user)

					return redirect('home:register')

		return render(request,self.template_name,{'form':form})
