from django.urls import  path
from .views import markets_view, markets_single_view

urlpatterns = [
    path('',markets_view),
    path('<int:pk>/',markets_single_view),
]
