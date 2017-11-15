from django.conf.urls import url, include
from . import views

urlpatterns = [
  url(r'^$', views.Home.as_view()),
  url(r'^products/$', views.product_list, name='product_list'),
]
