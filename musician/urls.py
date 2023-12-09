from django.urls import path

from . import views

urlpatterns = [
    path('', views.musician_views, name='musician'),
    path('edit/<int:id>', views.edit_musician, name='edit_musician'),
]
