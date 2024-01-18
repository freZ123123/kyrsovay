from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='home'),
     path('about-us', views.about, name='about'),
     path('range', views.range, name='range'),
     path('bays', views.bays, name='bays'),
     path('post/<int:post_id>/', views.show_posts, name='post'),
     path('delivery', views.delivery, name='delivery'),
     path('accept', views.delivery, name='accept'),



]