from django.urls import  path
from .views import MarketsView, markets_single_view, sellers_view, sellers_single_view

urlpatterns = [
    path('market/',MarketsView.as_view),
    path('market/<int:pk>/',markets_single_view, name = 'market-detail'),
    path('seller/',sellers_view),
    path('seller/<int:pk>/',sellers_single_view, name='seller_single')
]