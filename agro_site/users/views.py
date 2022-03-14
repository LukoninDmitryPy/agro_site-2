from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import CreationForm
from django.shortcuts import redirect, render
# from .models import Profile
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login
from .authentication import EmailAuthBackend
from .forms import LoginForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('sales_backend:index')
    template_name = 'users/signup.html'


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = EmailAuthBackend.authenticate(form, username=cd['username'], password=cd['password'])
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('sales_backend:index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


class Logout(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:logout')
    template_name = 'users/logged_out.html'


class PasswordChangeDone(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change_done.html'