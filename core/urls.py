from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registerUser, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/', views.profileUser, name="profile"),
    path('update_profile/', views.updateProfileUser, name="update_profile"),
    path('change_password/', views.changePassword, name="change_password"),
    path('set_password/', views.setPassword, name="set_password"),
]
