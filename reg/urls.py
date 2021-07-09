from django.urls import path
from reg import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('c19_info', views.c19_info, name="c19_info"),
    path('register_hsp', views.HspView.as_view(), name="register_hsp"),
    path('register_user', views.UsrView.as_view(), name="register_user"),
    path('sgin_hsp', views.sgin_hsp, name="sgin_hsp"),
    path('sgin_user', views.sgin_user, name="sgin_user"),
    path('sginpg_hsp', views.sginpg_hsp, name="sginpg_hsp"),
    path('sginpg_user', views.sginpg_user, name="sginpg_user"),
    path('search/', views.search, name="search"),
    path("hsp_edit", views.update_data, name="update_data"),
    path("usr_edit", views.update_usr_data, name="update_usr_data"),
    path("change_pass_usr", views.change_pass_usr, name="change_pass_usr"),
    path("change_pass_hsp", views.change_pass_hsp, name="change_pass_hsp"),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
    path('sout', views.sout, name="sout"),
]