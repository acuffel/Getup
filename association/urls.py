from django.urls import path
from association import views

app_name = 'association'

urlpatterns = [
    path('search', views.search_asso, name='search_asso'),
    path('search/c', views.search_by_country, name='search_country'),
    path('search/ci', views.search_by_city, name='search_city'),
    path('search/na', views.search_by_name, name='search_name'),
    path('home_association/<association_id>',
         views.home_asso, name='home_asso'),
    path('make_donation/<association_id>', views.make_donation,
         name='make_donation'),
    path('validate_donation/<association_id>/<email>/<amount>',
         views.validate_donation,
         name='validate_donation'),
]
