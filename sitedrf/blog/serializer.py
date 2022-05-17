from rest_framework import serializers
from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ['title', 'content' , 'cat']

""" class WomenSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_updete = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_create = validated_data.get('time_create', instance.time_create)
        instance.time_updete = validated_data.get('time_updete', instance.time_updete)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance """