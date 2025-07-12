from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filter


class TodoFilter(filter.FilterSet):
    class Meta:
        model = Todo
        fields = {
            'title': ['exact', 'icontains'],
            'is_completed': ['exact'],
            'created_time': ['exact', 'year__gt', 'year__lt'],
        }

class TodoViewSet(viewsets.ModelViewSet):
    # http_method_names = ['get']
    queryset = Todo.objects.all().order_by('-created_time')
    serializer_class = TodoSerializer
    filterset_class = TodoFilter

    def create(self, request, *args, **kwargs):

        # print(request.data)
        request_data= request.data
        # request_data['title'] = f'python_course_-{request_data['title']}'

        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
