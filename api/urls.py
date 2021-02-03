# myapi/urls.py

from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_jwt.views import verify_jwt_token

router = routers.DefaultRouter()
router.register(r'users1', views.UserViewSet)
router.register(r'meters', views.MeterViewSet)
router.register(r'reading', views.ReadingViewSet)
router.register(r'usermeters', views.UserMeterViewSet)
router.register(r'test', views.TestModelViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('users/', include('users.urls')),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('token-verify/', verify_jwt_token),
]