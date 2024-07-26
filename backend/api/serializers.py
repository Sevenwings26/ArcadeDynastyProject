from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Event, Ticket, Gallery, Review, BlogPost, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {"password": {"write_only":True}}

    def create(self, validated_data):
        user = User(
            email= validated_data['email'],
            username= validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class EventSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'image', 'categories', 'created_at', 'updated_at']

class TicketSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'user', 'event', 'ticket_type', 'price', 'purchase_date', 'is_paid', 'payment_reference']

class GallerySerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = Gallery
        fields = ['id', 'event', 'image', 'caption', 'uploaded_at']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'event', 'rating', 'comment', 'created_at']

class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at', 'featured_image']

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_date', 'total_amount', 'is_paid', 'payment_reference', 'tickets']
