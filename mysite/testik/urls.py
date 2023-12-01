from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from mysite.testik.views import *
from mysite.home import views
app_name = 'testik'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('Sertif/', SertifView.as_view(), name='Sertif'),
    path('Sertif/update/<int:pk>/', SertifUpdate.as_view(), name='SertifUpdate'),
    path('Sertif/detail/<int:pk>/', SertifDetail.as_view(), name='SertifDetail'),
    path('Sertif/create/', SertifCreate.as_view(), name='SertifCreate'),
    path('Sertif/delete/<int:pk>/', SertifDelete.as_view(), name='SertifDelete'),
]
