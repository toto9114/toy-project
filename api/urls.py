from django.urls import path
from api import views

urlpatterns = [
    path('health', views.health),
    path('create_user', views.UserAPIView.as_view()),
    path('user_places', views.UserPlaceView.as_view()),
    path('search_place', views.SearchPlaceView.as_view()),
    path('save_place', views.SavePlaceView.as_view()),
    path('update_place_description/<int:place_id>', views.PlaceDescriptionView.as_view()),
]