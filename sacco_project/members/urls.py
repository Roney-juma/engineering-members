from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, MemberLoginView  , EventViewSet,BlogViewSet

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'events', EventViewSet)
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MemberLoginView.as_view(), name='member-login'), 
]
