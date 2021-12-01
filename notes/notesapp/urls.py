from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_notes, name='show_notes'),
    path('<int:note_id>/', views.show_note, name='show_note'),
    path('new_note/', views.new_note, name='new_note'),
]