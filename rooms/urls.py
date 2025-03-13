from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  RoomViewSet,PhotoGalleryViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'photo', PhotoGalleryViewSet)
# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
    ]