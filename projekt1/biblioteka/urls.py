from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('userAuth/', views.userAuth, name='userAuth'),
    path('panel/', views.userPanel, name='panel'),
    path('panel/upload/', views.upload, name='upload'),
    path('panel/logout_view/', views.logout_view, name='logout_view'),
    path('panel/create/', views.create, name='create'),
    path('panel/<int:pk>/update/', views.update, name='udpateBook'),
    path('<int:pk>/update/', views.update_database, name='update_database'),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('panel/<int:pk>/delete/', views.delete, name='delete'),

]