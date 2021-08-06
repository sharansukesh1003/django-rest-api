from django.urls import path
from . import views

urlpatterns=[
    path('',views.get_routes),
    path('notes/',views.get_notes),
    path('notes/create/',views.create_note),
    path('notes/<int:pk>',views.get_note),
    path('notes/update/<int:pk>',views.update_note),
    path('notes/delete/<int:pk>',views.delete_note),
]