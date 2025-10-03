from django.urls import path
from .import views

urlpatterns = [
    path('blog/', views.index, name= 'Blog post'),
    path('post_detail/<int:pk>/', views.post_detail, name= 'Post detail'),
    path('post_edit/<int:pk>/', views.post_edit, name= 'Post edit'),
    path('post_delete/<int:pk>/', views.post_delete, name= 'Post delete'),
    path('post/<int:post_id>/<str:value>/', views.react_to_post, name='react_to_post'),
    
  
    

]
