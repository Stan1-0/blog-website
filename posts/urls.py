from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pos/<string:pk>t',views.post, name='post')
]
