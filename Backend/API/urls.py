from django.urls import path
from . import views

urlpatterns = [
    path('',views.create),
    # path('update/<int:pk>',views.update),
    # path("Get/<pk>/",views.GetOne)
]
