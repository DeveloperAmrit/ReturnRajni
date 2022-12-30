from django import views
from django.urls import path
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path("" , views.index , name="index"),
    path('about',views.aboutus,name='shopAboutUs'),

    path('signing', views.showSignIn , name='signing'),
    path('logging', views.showLogIn, name='logging'),

    path('signin', views.signIn , name='signin'),
    path('login', views.logIn , name='signin'),

    path('feedback',views.userFeedback,name='feedback')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
