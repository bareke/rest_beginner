from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import HelloApiView
from .views import HelloViewSet

# Create your urls here.


router = DefaultRouter()

router.register('hello-viewset', HelloViewSet, basename='hello-viewset')


urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls))
]