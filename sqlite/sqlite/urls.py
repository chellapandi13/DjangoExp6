# your_project/urls.py
from django.contrib import admin
from django.urls import path, include  # Make sure include is imported
from dbapp import views

urlpatterns = [
     path('', views.home, name='home'),  # Homepage URL
    path('admin/', admin.site.urls),
    path('dbapp/', include('dbapp.urls')),  # Make sure this is correct
]
