from django.urls import path
from . import views

urlpatterns= [
    path('',views.mostrar_todos_los_productos),
    path('new/', views.create_product, name='create_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('update_product/<int:id>/', views.update, name='update'),
] 