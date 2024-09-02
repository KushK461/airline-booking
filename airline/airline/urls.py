from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from myapp.views import FlightViewSet, PassengerViewSet

router = DefaultRouter()
router.register(r'flights', FlightViewSet)
router.register(r'passengers', PassengerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
