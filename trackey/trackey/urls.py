"""
URL configuration for trackey project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from API_keys import views
from API_keys.views import CoproprieteViewset, CommonKeyViewset, PrivateKeyViewset, TrackCommonViewset, TrackPrivateViewset, AgencyUpdateView, AgencyCreateView, ChangePasswordView, getUpdateCommonTracKey, getUpdatePrivateTracKey, getAccount, SendOTPView, VerifyOTPView,  sendMPoublie, changeMPoublie, DeleteAccountView
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


router = routers.SimpleRouter()
router.register('Copropriete', CoproprieteViewset, basename='Copropriete')
router.register('CommonKey', CommonKeyViewset, basename='CommonKey')
router.register('PrivateKey', PrivateKeyViewset, basename='PrivateKey')
router.register('TrackCommon', TrackCommonViewset, basename='TrackCommon')
router.register('TrackPrivate', TrackPrivateViewset, basename='TrackPrivate')




urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.getRoutes),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/MPoublie/get', views.sendMPoublie, name='send_MpOublie' ),
    path('api/MPoublie/post', views.changeMPoublie, name='post_MpOublie' ),
    path('api/otp', SendOTPView.as_view(), name='sendtoken_otp' ),
    path('api/otp/verify', VerifyOTPView.as_view(), name='checktoken_otp' ),
    path('api/user/update', AgencyUpdateView.as_view(), name='udpate_user'),
    path('api/user/create', AgencyCreateView.as_view(), name='create_user'),
    path('api/user/account', views.getAccount, name='get_account'),
    path('api/user/password', ChangePasswordView.as_view(), name='change_password'), 
    path('api/user/delete', DeleteAccountView.as_view(), name='delete_password'), 
    path('api/TrackC/update/<int:key_id>/', views.getUpdateCommonTracKey, name='track-update'),
    path('api/TrackP/update/<int:key_id>/', views.getUpdatePrivateTracKey, name='track-update')
    ]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
