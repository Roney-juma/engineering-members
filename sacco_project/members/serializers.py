from rest_framework import serializers
from .models import Member, Event, EventImage,Blog
from django.contrib.auth import authenticate

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        print("username",username,password )
        if username and password:
            
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Username and password are required.")
        
        return attrs

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['id', 'image', 'uploaded_at']

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, required=False)

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'created_at', 'updated_at', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        event = Event.objects.create(**validated_data)
        for image_data in images_data:
            EventImage.objects.create(event=event, **image_data)
        return event

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        instance = super().update(instance, validated_data)

        for image in uploaded_images:
            EventImage.objects.create(event=instance, image=image)
        
        return instance
    
class BlogSerializer(serializers.ModelSerializer):
    content = serializers.CharField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content','description','author', 'image', 'published_date']