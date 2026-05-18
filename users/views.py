from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from django.shortcuts import redirect
from . import models, forms


class RegisterView(generic.CreateView):
    template_name = 'users/register.html'
    form_class = forms.RegisterForm
    success_url = '/login/'


class AuthLoginView(generic.FormView):
    template_name = 'users/login.html'
    form_class = forms.LoginForm
    success_url = '/user_list/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class AuthLogoutView(generic.View):

    def get(self, request):
        logout(request)
        return redirect('/login/')


class UserListView(generic.ListView):
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    model = models.CustomUser