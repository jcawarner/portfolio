from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('webdevelopment/', views.webdevelopment, name='webdevelopment'),
    path('gui/', views.gui, name='gui'),
    path('gui/projects/<str:project>', views.projects, name='projects'),
    path('website/', views.website, name='website'),

]
