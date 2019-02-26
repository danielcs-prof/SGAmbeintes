from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_embedded, name='list_embedded'),
    path('new/', views.new_embedded, name='new_embedded'),
    path('update/<int:pk>/', views.update_embedded, name='update_embedded'),
    path('delete/<int:pk>/', views.delete_embedded, name='delete_embedded'),

]