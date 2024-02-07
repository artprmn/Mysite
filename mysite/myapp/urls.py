# myapp/urls.py
from django.urls import path
from .views import home, user_page, register, user_login, user_logout
from .views import campaign_detail, edit_profile, campaign_statistics
from .views import user_profile, create_campaign, create_house, delete_house
from .views import enter_apartment_visit, house_detail, add_house, delete_campaign

urlpatterns = [
    path('', home, name='home'),
    path('user/<str:username>/', user_page, name='user_page'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='user_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/create_campaign/', create_campaign, name='create_campaign'),
    path('profile/create_house/<int:campaign_id>/', create_house, name='create_house'),
    path('campaign/<int:campaign_id>/', campaign_detail, name='campaign_detail'),
    path('enter_apartment_visit/<int:house_id>/', enter_apartment_visit, name='enter_apartment_visit'),
    path('house_detail/<int:house_id>/', house_detail, name='house_detail'),
    path('campaign/<int:campaign_id>/add_house/', add_house, name='add_house'),
    path('campaign/<int:campaign_id>/delete/', delete_campaign, name='delete_campaign'),
    path('house/<int:house_id>/delete/', delete_house, name='delete_house'),
    path('campaign/statistics/', campaign_statistics, name='campaign_statistics'),

]
