from django.contrib import admin
from django.urls import path
from regandloginapp.views import Home, RegisterInput, Register, LoginInput, Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', Home.as_view()),
    path('registerinput', RegisterInput.as_view()),
    path('register', Register.as_view()),
    path('logininput', LoginInput.as_view()),
    path('login', Login.as_view())
]