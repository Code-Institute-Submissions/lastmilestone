from django.urls import path

from . import views

urlpatterns = [
    path('', views.schedule, name='all_comments'),
    path('<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('add/', views.add_comment, name='add_comment'),
    path('edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
]