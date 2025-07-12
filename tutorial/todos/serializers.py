from rest_framework import serializers
from .models import Todo



class TodoSerializer(serializers.ModelSerializer):
#    title = serializers.CharField(required=True)


    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ['id', 'title', 'kind', 'description', 'is_completed', 'created_time'] 一個個的打法
