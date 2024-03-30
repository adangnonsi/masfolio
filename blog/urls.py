
from django.urls import path

from blog import views




urlpatterns = [
  
    path('blog_vue/', views.blog, name="vue_blog"),
    path('categoris/<slug:category>/', views.blog, name='category_blog'),
    path('detail_b/<int:my_id>/', views.blog_detail, name="detail_blog"),
     

]


