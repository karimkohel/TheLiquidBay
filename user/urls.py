from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView

app_name = 'user'

urlpatterns = [
	path('register/',views.register,name='register'),
	path('login/',LoginView.as_view(template_name='user/login.html'),name='login'),
	path('logout/',LogoutView.as_view(template_name='user/logout.html'),name='logout'),
	path('profile/',views.profile,name='profile'),
	path('profil-edit/',views.profile_edit,name='profile_edit'),
	# path('password-reset/',PasswordResetView.as_view(template_name='user/password_reset.html'),name='password_reset'),
	# path('password-reset/done/',PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
	# path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
]