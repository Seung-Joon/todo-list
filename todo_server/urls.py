"""todo_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from todo.views import TodoViewSet
from user.views import UserViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('todo', TodoViewSet)

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="TodoList Open API",
        default_version='v1',
        description="Todolist Api Documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tmdwns02556@google.com"),
        license=openapi.License(name="Seung-Joon"),
    ),
    validators=['flex'], #'ssv'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=router.urls,
)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)/v1$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/v1/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/v1/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]   