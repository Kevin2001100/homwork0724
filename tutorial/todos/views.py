from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters import rest_framework as filter
from .models import Todo, Student, Teacher
from .serializers import TodoSerializer, StudentSerializer, TeacherSerializer

# Todo 篩選器
class TodoFilter(filter.FilterSet):
    class Meta:
        model = Todo
        fields = {
            'title': ['exact', 'icontains'],
            'is_completed': ['exact'],
            'created_time': ['exact', 'year__gt', 'year__lt'],
        }

# Todo CRUD + 篩選 + 回應格式
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_time')
    serializer_class = TodoSerializer
    filterset_class = TodoFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "message": "新增成功",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "更新成功",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": "刪除成功"
        }, status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save()

# Teacher CRUD
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# Student CRUD + 進階驗證
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception:
            return Response({"error": "找不到該學生"}, status=404)

    def create(self, request, *args, **kwargs):
        teacher_id = request.data.get('teacher_id')
        if not teacher_id or not self.get_teacher(teacher_id):
            return Response({"error": "找不到對應的老師 ID"}, status=400)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        teacher_id = request.data.get('teacher_id')
        if teacher_id and not self.get_teacher(teacher_id):
            return Response({"error": "找不到對應的老師 ID"}, status=400)
        return super().update(request, *args, **kwargs)

    def get_teacher(self, teacher_id):
        return Teacher.objects.filter(id=teacher_id).first()

