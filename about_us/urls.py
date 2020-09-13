from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.about_us, name='about_us') ,
    path('<int:trainer_id>/', views.trainer_detail, name='trainer_detail'),
    path('add/', views.add_trainer, name='add_trainer'),
    path('edit/<int:trainer_id>/', views.edit_trainer, name='edit_trainer'),
    path('delete/<int:trainer_id>/',
         views.delete_trainer, name='delete_trainer'),
]