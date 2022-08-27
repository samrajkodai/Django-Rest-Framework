from django.urls import path
from . import views

urlpatterns = [
    # path('',views.api_home)
     path('<int:pk>/',views.ProductDetailAPIView.as_view()),
     path('',views.ProductCreateAPIView.as_view()),
      path('list',views.ProductListAPIView.as_view()) 
]
