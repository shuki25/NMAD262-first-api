from rest_framework import routers

from app import api_views as views

router = routers.DefaultRouter()
router.register("students", views.StudentViewSet)
