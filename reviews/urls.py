from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  ReviewViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)
# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]