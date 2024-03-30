

from django.urls import path

from monapp import views

urlpatterns = [
    
    path('', views.home, name='home'),

    path('categorie/<slug:category>/', views.home, name='category_home'),
    path('service/', views.service, name='service'),
    path('contact/', views.vue_contact, name='contact'),
    path('detail_portfolio/<int:my_id>/', views.portfolio_detail, name='detail_de_portfolio'),


    
]


