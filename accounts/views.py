from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from braces import views
 
from .forms import LoginForm #, RegistrationForm



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

		if user is not None and user.is_active():
			login(self.request, user)
			return super().form_valid(form)
		else:
			return self.form_invalid(form)



class SignUpView(generic.TemplateView):
	template_name = 'accounts/signup.html'



class LogoutView(generic.TemplateView):
	pass



class DashboardView(generic.TemplateView):
	template_name = 'accounts/dashboard.html'
