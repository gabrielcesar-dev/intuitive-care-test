from django.urls import path
from .views import SearchOperators, LoadCSVData

urlpatterns = [
    path('operators/search/', SearchOperators.as_view(), name='search_operators'),
    path('operators/load-data/', LoadCSVData.as_view(), name='load_data'),
]