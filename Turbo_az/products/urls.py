from django.urls import path
from products import views

urlpatterns = [
  path('', views.index, name = "index"),
  path('upload/', views.image_upload_view, name = "img"),
]