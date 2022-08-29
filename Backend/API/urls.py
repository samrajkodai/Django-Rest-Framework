from django.urls import path
from . import views

urlpatterns = [
    path('',views.create),
    path('get/<int:pk>',views.get_one),
    path("update/<int:pk>/",views.update),
    path("delete/<int:pk>/",views.delete)
]
