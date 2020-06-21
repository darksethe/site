"""Academia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',RedirectView.as_view(url='/index/')),
    path('index/',views.Inicio),
    path('index/treinar/',views.Treinamento),
    path('index/assinar/',views.Aulas),
    path('index/assinar/submit',views.Cadastrar),
    path('login/',views.login_user),
    path('login/submit',views.submit_login),
    path('lista/',views.Lista),
    path('lista_admin/',views.Lista_admin),
    path('delete/<int:cpf>',views.delete),
    path('delete/lista_admin/',views.Lista_admin),
    path('login/lista/',views.Lista),
    path('lista/submit',views.Pessoas),

]
