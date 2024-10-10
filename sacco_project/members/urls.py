from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, MemberLoginView  , ProjectViewSet

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'projects', ProjectViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MemberLoginView.as_view(), name='member-login'), 
]
