"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from mysite.anketa.views import *
from mysite.home import views
app_name = 'anketa'
urlpatterns = [
    path('professions/', ProfessionsView.as_view(), name='professions'),
    path('professions/update/<int:pk>/', ProfessionUpdate.as_view(), name='ProfessionUpdate'),
    path('professions/detail/<int:pk>/', ProfessionDetail.as_view(), name='ProfessionDetail'),
    path('professions/create/', ProfessionCreate.as_view(), name='ProfessionCreate'),
    path('professions/delete/<int:pk>/', ProfessionDelete.as_view(), name='ProfessionDelete'),

    path('skills/', SkillsView.as_view(), name='skills'),
    path('skills/update/<int:pk>/', SkillsUpdate.as_view(), name='SkillsUpdate'),
    path('skills/detail/<int:pk>/', SkillsDetail.as_view(), name='SkillsDetail'),
    path('skills/create/', SkillsCreate.as_view(), name='SkillsCreate'),
    path('skills/delete/<int:pk>/', SkillsDelete.as_view(), name='SkillsDelete'),

    path('questions/', QuestionsView.as_view(), name='questions'),
    path('questions/update/<int:pk>/', QuestionsUpdate.as_view(), name='QuestionsUpdate'),
    path('questions/detail/<int:pk>/', QuestionsDetail.as_view(), name='QuestionsDetail'),
    path('questions/create/', QuestionsCreate.as_view(), name='QuestionsCreate'),
    path('questions/delete/<int:pk>/', QuestionsDelete.as_view(), name='QuestionsDelete'),

    path('model_prof/', Model_profView.as_view(), name='model_prof'),
    path('model_prof/update/<int:pk>/', Model_profUpdate.as_view(), name='Model_profUpdate'),
    path('model_prof/detail/<int:pk>/', Model_profDetail.as_view(), name='Model_profDetail'),
    path('model_prof/create/', Model_profCreate.as_view(), name='Model_profCreate'),
    path('model_prof/delete/<int:pk>/', Model_profDelete.as_view(), name='Model_profDelete'),

    path('human/', HumanView.as_view(), name='human'),
    path('human/update/<int:pk>/', HumanUpdate.as_view(), name='HumanUpdate'),
    path('human/detail/<int:pk>/', HumanDetail.as_view(), name='HumanDetail'),
    path('human/create/', HumanCreate.as_view(), name='HumanCreate'),
    path('human/delete/<int:pk>/',HumanDelete.as_view(), name='HumanDelete'),
    
    path('blank/', BlankView.as_view(), name='blank'),
    path('blank/update/<int:pk>/', BlankUpdate.as_view(), name='BlankUpdate'),
    path('blank/detail/<int:pk>/', BlankDetail.as_view(), name='BlankDetail'),
    path('blank/create/', BlankCreate.as_view(), name='BlankCreate'),
    path('blank/delete/<int:pk>/', BlankDelete.as_view(), name='BlankDelete'),

]
