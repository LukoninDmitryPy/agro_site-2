# from django.views.generic import CreateView

# from django.urls import reverse_lazy

# from .forms import CreationForm, UserEditForm, ProfileEditForm, UserRegistrationForm
# from django.shortcuts import redirect, render
# from .models import Profile
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.contrib.auth import login
# from .authentication import EmailAuthBackend
# from .forms import LoginForm


# class SignUp(CreateView):
#     form_class = CreationForm
#     success_url = reverse_lazy('sales_backend:index')
#     template_name = 'users/signup.html'

# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password'])
#             # Save the User object
#             new_user.save()
#             profile = Profile.objects.create(user=new_user)
#             return render(request, 'users/register_done.html', {'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'users/register.html', {'user_form': user_form})

# def edit(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#         return render(request,
#                       'users/edit.html',
#                       {'user_form': user_form,
#                        'profile_form': profile_form})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = EmailAuthBackend.authenticate(form, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('sales_backend:index')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'users/login.html', {'form': form})

# class Login(CreateView):
#     form_class = LoginForm
#     template_name = 'users/login.html'


# class Logout(CreateView):
#     form_class = CreationForm
#     success_url = reverse_lazy('users:logout')
#     template_name = 'users/logged_out.html'


# class PasswordChangeDone(CreateView):
#     form_class = CreationForm
#     success_url = reverse_lazy('users:password_change_done')
#     template_name = 'users/password_change_done.html'


from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})