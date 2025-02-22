# -*- coding: utf-8 -*-
"""curso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import CursoAPIView, AvaliacaoAPIView, CursosAPIView, AvaliacoesAPIView

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/<int:pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
]
