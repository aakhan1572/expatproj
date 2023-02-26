from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.expads, name='expads'),
    path('category/<slug:slug>/', views.expads, name='expads_by_category'),
    path('expatad/<int:id>/', views.expataddetail, name='expataddetail'),

    #path('<slug:slug>/', views.store, name='products_by_category'),
    #path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    #path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    #path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('addads/', views.addads, name='addads'),
    path('contactme/', views.contactme, name='contactme'),
    path('contactyou/', views.contactyou, name='contactyou'),
    path('contactmes/', views.contactmes, name='contactmes'),
    path('interested/', views.interested, name='interested'),

    #path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),

]