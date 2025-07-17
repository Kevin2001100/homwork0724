from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# 導入三個 ViewSet
from tutorial.todos.views import TodoViewSet, StudentViewSet, TeacherViewSet

# router 註冊
router = DefaultRouter(trailing_slash=False)  # 建議統一 trailing_slash
router.register(r'todos', TodoViewSet, basename='todo')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'teachers', TeacherViewSet, basename='teacher')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),  # 統一 API 前綴
]
