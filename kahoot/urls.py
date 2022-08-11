from django.contrib import admin
from django.urls import path, include, re_path
from kahootApi.views import UserAPIList, UserAPIUpdate, UserAPIDestroy
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/user/', UserAPIList.as_view()),
    path('api/v1/user/<int:pk>/', UserAPIUpdate.as_view()),
    path('api/v1/userdelete/<int:pk>/', UserAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)