from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from braces import views
 
from .forms import LoginForm, RegistrationForm, UserEditForm
from tickets.models import FilmTicket, TheaterTicket, ConcertTicket


# AnonymousRequiredMixin:
# 	Only Anonymous users can visit it,
# 	logged in user will be redirected

# FormView:
# 	Will create form object of the given model, later this form
#	will be showen in the given template

# login view
class LoginView(views.AnonymousRequiredMixin,
	views.FormValidMessageMixin, generic.FormView):

	# a form to send it to context
	form_class = LoginForm
	# use User as model
	model = User
	# on success will go to this url
	success_url = reverse_lazy('tickets:home')
	# used template
	template_name = 'accounts/login.html'
	# this message will be seen on successfull login
	form_valid_message = 'شما با موفقیت وارد سایت پاج تیکت شدید'

	def form_valid(self, form):
		# get username and password
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')

		# authentica user
		user = authenticate(username=username, password=password)

		# if user is authenticate and active, then login
		# else: render the form will the errors
		if user is not None and user.is_active:
			login(self.request, user)
			return super().form_valid(form)
		else:
			return self.form_invalid(form)


# sign up view
class SignUpView(views.AnonymousRequiredMixin, views.FormValidMessageMixin,
	generic.CreateView):
	# a form to send it to context
	form_class = RegistrationForm
	# used template
	template_name = 'accounts/signup.html'
	# use User as model
	model = User
	# on success will go to this url
	success_url = reverse_lazy('accounts:login')
	# this message will be seen on successfull login
	form_valid_message = 'شما در سایت پاج تیکت عضو شدید. اکنون می توانید وارد سایت شوید'


# log out view
class LogoutView(views.LoginRequiredMixin, generic.RedirectView):
	# on success will go to this url
	url = reverse_lazy('tickets:home')

	def get(self, request, *args, **kwargs):
		# logout user
		logout(request)
		# return user to home page (the given `url`)
		return super().get(request, *args, **kwargs)


# dashboard view
class DashboardView(views.LoginRequiredMixin, generic.TemplateView):
	# used template
	template_name = 'accounts/dashboard.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# get all films, theaters and concerts tickets 
		# that belong to current user from database
		films = FilmTicket.objects.filter(user=self.request.user)
		theaters = TheaterTicket.objects.filter(user=self.request.user)
		concerts = ConcertTicket.objects.filter(user=self.request.user)

		# calculate total bought ticket
		total_tickets = films.count()
		total_tickets += theaters.count()
		total_tickets += concerts.count()

		# send films, theaters, concerts and total ticket
		# also time
		context['film_tickets'] = films
		context['theater_tickets'] = theaters
		context['concert_tickets'] = concerts
		context['total_tickets'] = total_tickets
		context['now'] = timezone.now()
		return context


# user edit view
class UserEditView(views.LoginRequiredMixin,
	views.FormValidMessageMixin,
	generic.edit.UpdateView):
	
	# used template
	template_name = 'accounts/user_edit.html'
	# a form to send it to context
	form_class = UserEditForm
	# use User as model
	model = User
	# on success will go to this url
	success_url = reverse_lazy('accounts:dashboard')
	# this message will be seen on successfull login
	form_valid_message = 'اطلاعات کاربری با موفقیت بروزرسانی شدند'

	def get_object(self):
		return self.request.user
