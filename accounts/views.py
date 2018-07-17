from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from braces import views
 
from .forms import LoginForm, RegistrationForm



class LoginView(views.AnonymousRequiredMixin,
	views.FormValidMessageMixin, generic.FormView):

	form_class = LoginForm
	model = User
	success_url = reverse_lazy('tickets:home')
	template_name = 'accounts/login.html'
	form_valid_message = 'شما با موفقیت وارد سایت شدید'

	def form_valid(self, form):
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')

		user = authenticate(username=username, password=password)

		if user is not None and user.is_active:
			login(self.request, user)
			return super().form_valid(form)
		else:
			return self.form_invalid(form)



class SignUpView(views.AnonymousRequiredMixin, views.FormValidMessageMixin,
	generic.CreateView):
	form_class = RegistrationForm
	template_name = 'accounts/signup.html'
	model = User
	success_url = reverse_lazy('accounts:login')
	form_valid_message = ''




class LogoutView(views.LoginRequiredMixin, generic.RedirectView):
	url = reverse_lazy('tickets:home')

	def get(self, request, *args, **kwargs):
		logout(request)
		return super().get(request, *args, **kwargs)



class DashboardView(generic.TemplateView):
	template_name = 'accounts/dashboard.html'
