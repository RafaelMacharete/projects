from django.urls import path
from . import views
from .views import post, edit, update, delete

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', post, name='post'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]