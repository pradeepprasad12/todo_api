
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from django.contrib.auth import views as auth_views

from todo.views import TodoListView, TodoDetailView

router = routers.DefaultRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="Todo API",
      default_version='v1',
      description="APIs for managing todo items",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@todo.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/', include(router.urls)),
    path('api/todo/', TodoListView.as_view(), name='todo-list'),
    path('api/todo/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]