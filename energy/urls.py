"""
URL configuration for energy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.schema import schema

schema_view = get_schema_view(
    openapi.Info(
        title="Microservice Energy",
        default_version='v1',
        description="API for Microservice Energy",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="ananias.nobrega@gmail.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=False,
    permission_classes=(BasePermission,),
)

urlpatterns = [
    path('', include('supplier.api.urls')),

    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),

    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)), name='graphql'),

    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
