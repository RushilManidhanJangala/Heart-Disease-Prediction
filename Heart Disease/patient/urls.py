from django.urls import path
from .import views
urlpatterns=[
    path('login',views.login,name="login"),
    path('about',views.about,name="about"),
    path('blog',views.blog,name="blog"),
    path('contact',views.contact,name="contact"),
    path('index',views.index,name="index"),
    path('support',views.support,name="support"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    ]