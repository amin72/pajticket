from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from braces import views
 
from .forms import LoginForm, RegistrationForm, UserEditForm
from tickets.models import FilmTicket, TheaterTicket, ConcertTicket


class LoginView(views.AnonymousRequiredMixin,
	views.FormValidMessageMixin, generic.FormView):

	form_class = LoginForm
	model = User
	success_url = reverse_lazy('tickets:home')
	template_name = 'accounts/login.html'
	form_valid_message = 'شما با موفقیت وارد سایت پاج تیکت شدید'

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
	form_valid_message = 'شما در سایت پاج تیکت عضو شدید. اکنون می توانید وارد سایت شوید'



class LogoutView(views.LoginRequiredMixin, generic.RedirectView):
	url = reverse_lazy('tickets:home')

	def get(self, request, *args, **kwargs):
		logout(request)
		return super().get(request, *args, **kwargs)


class DashboardView(views.LoginRequiredMixin, generic.TemplateView):
	template_name = 'accounts/dashboard.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		films = FilmTicket.objects.filter(user=self.request.user)
		theaters = TheaterTicket.objects.filter(user=self.request.user)
		concerts = ConcertTicket.objects.filter(user=self.request.user)

		total_tickets = films.count()
		total_tickets += theaters.count()
		total_tickets += concerts.count()

		context['film_tickets'] = films
		context['theater_tickets'] = theaters
		context['concert_tickets'] = concerts
		context['total_tickets'] = total_tickets
		context['now'] = timezone.now()
		return context



class UserEditView(views.LoginRequiredMixin,
	views.FormValidMessageMixin,
	generic.edit.UpdateView):
	
	template_name = 'accounts/user_edit.html'
	form_class = UserEditForm
	model = User
	success_url = reverse_lazy('accounts:dashboard')
	form_valid_message = 'اطلاعات کاربری با موفقیت بروزرسانی شدند'

	def get_object(self):
		return self.request.user
