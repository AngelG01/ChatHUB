from django.urls import path

from ChatHUB.users import views

urlpatterns = [
    path('login/', views.SignUpView.as_view(), name='login'),

]
