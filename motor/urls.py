from django.urls import path

from .views import PostsListView, PostDetailsView


urlpatterns = [
    path('', PostsListView.as_view(), name='motor_api'),
    path('<int:pk>', PostDetailsView.as_view(), name='maintenance_details_api'),
    ]