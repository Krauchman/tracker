from django.urls import path, include

from rest_framework import routers

from .views import TaskViewSet, StatusChangeViewSet, StatusChangeCreateAPIView


router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('statuses', StatusChangeViewSet)


urlpatterns = [
    path('change_status/', StatusChangeCreateAPIView.as_view()),
    path('', include(router.urls)),
]
