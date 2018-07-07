from django.shortcuts import render
from django.views import generic

 

class LoginView(generic.TemplateView):
	template_name = 'accounts/login.html'



class SignUpView(generic.TemplateView):
	template_name = 'accounts/signup.html'



class LogoutView(generic.TemplateView):
	pass



class DashboardView(generic.TemplateView):
	template_name = 'accounts/dashboard.html'
