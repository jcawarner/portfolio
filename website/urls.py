from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('webdevelopment/', views.webdevelopment, name='webdevelopment'),
    path('gui/', views.gui, name='gui'),
    path('gui/projects/<str:project>', views.projects, name='projects'),
    path('website/', views.website, name='website'),
    path('contact/', views.contact, name='contact'),
    path('contact/success', views.success, name='success'),
    path('freelancing/projects/<str:freelancing_project>', views.freelancing_projects, name='freelancing'),

]
