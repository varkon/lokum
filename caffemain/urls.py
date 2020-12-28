from django.urls import path
from . import views
from shop import views as sh

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<slug:category_slug>/', sh.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', sh.product_detail, name='product_detail'),

    ]
