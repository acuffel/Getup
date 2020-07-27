from django.urls import path
from association import views

app_name = 'association'

urlpatterns = [
    path('search', views.search_asso, name='search_asso'),
    path('search/c', views.search_by_country, name='search_country'),
    path('search/ci', views.search_by_city, name='search_city'),
    path('search/na', views.search_by_name, name='search_name'),
]
