from rest_framework import serializers
from todolist.models import TodoItem

class todItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'