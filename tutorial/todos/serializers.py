from rest_framework import serializers
from .models import Todo, Student, Teacher

# Todo CRUD Serializer
class TodoSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(required=True)  # 若你想強制驗證可打開這行

    class Meta:
        model = Todo
        fields = '__all__'
        # 或明確指定欄位：
        # fields = ['id', 'title', 'kind', 'description', 'is_completed', 'created_time']

# Teacher CRUD Serializer
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'class_name']

# Teacher 簡易顯示用（給 Student 回傳嵌套使用）
class TeacherSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'class_name']

# Student Serializer，teacher 為嵌套 read_only 顯示，teacher_id 提供寫入
class StudentSerializer(serializers.ModelSerializer):
    teacher = TeacherSimpleSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), write_only=True, source='teacher', required=False
    )

    class Meta:
        model = Student
        fields = ['id', 'name', 'teacher', 'teacher_id']
