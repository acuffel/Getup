from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('registration/member', views.member_registration,
         name='member_registration'),
    path('registration/association', views.association_registration,
         name='association_registration'),
    path('', views.logout_view, name='logout'),
    path('welcome/association', views.welcome_association,
         name='welcome_association'),
    path('info/association', views.show_information, name='show_information'),
    path('my_association', views.show_association, name='show_association'),
    path('my_association/update_asso', views.asso_upload_view,
         name='update_asso'),
]
