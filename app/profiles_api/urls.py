from django.urls import path

from .views import HelloApiView

# Create your urls here.


urlpatterns = [
    path('hello-view/', HelloApiView.as_view())
]