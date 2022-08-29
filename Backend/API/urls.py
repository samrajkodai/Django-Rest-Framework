from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('snippets/', views.SnippetList.as_view()),
    path('snippets/', views.TransformerList.as_view()),

    path("main/<int:pk>/",views.MainView.as_view())
]

