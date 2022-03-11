# from django.contrib.auth.views import (LoginView, LogoutView,
#                                        PasswordChangeDoneView,
#                                        PasswordChangeView,
#                                        PasswordResetCompleteView,
#                                        PasswordResetConfirmView,
#                                        PasswordResetDoneView,
#                                        PasswordResetView)

# from django.urls import path

# from . import views

# app_name = 'users'

# urlpatterns = [
#     path('register/', views.SignUp.as_view(), name='register'),
#     path('signup/', views.register, name='signup'),
#     path(
#         'logout/',
#         LogoutView.as_view(template_name='users/logged_out.html'),
#         name='logout'
#     ),
#     path(
#         'login/',
#         views.Login.as_view(
#             template_name='users/login.html'
#         ),
#         name='login'
#     ),
#     path(
#         'password_change/',
#         PasswordChangeView.as_view(
#             template_name='users/password_change_form.html'
#         ),
#         name='password_change_form'
#     ),
#     path(
#         'password_change/done/',
#         PasswordChangeDoneView.as_view(
#             template_name='users/password_change_done.html'
#         ),
#         name='password_change_done'
#     ),
#     path(
#         'password_reset/',
#         PasswordResetView.as_view(
#             template_name='users/password_reset_form.html'
#         ),
#         name='password_reset_form'
#     ),
#     path(
#         'password_reset/done/',
#         PasswordResetDoneView.as_view(
#             template_name='users/password_reset_done.html'
#         ),
#         name='password_reset_done'
#     ),
#     path(
#         'reset/<uidb64>/<token>/',
#         PasswordResetConfirmView.as_view(
#             template_name='users/password_reset_confirm.html'
#         ),
#         name='password_reset_confirm'
#     ),
#     path(
#         'reset/done/',
#         PasswordResetCompleteView.as_view(
#             template_name='users/password_reset_complete.html'
#         ),
#         name='password_reset_complete'
#     ),
#     path(
#         'edit/',
#         views.edit,
#         name='edit'
#     ),
# ]

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
]