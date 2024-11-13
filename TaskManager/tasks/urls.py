from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_view, name="index_view"),
    path('create/', views.create_view, name='create'),
    path('list/', views.list_view, name='list'),
    path('edit/<int:task_id>', views.edit_view, name='edit'),
    path('delete/<int:task_id>', views.delete_view, name='delete'),
    
]
