from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import (
    UserSerializer, CategorySerializer, EventSerializer, TicketSerializer, 
    GallerySerializer, ReviewSerializer, BlogPostSerializer, OrderSerializer
)
from .models import Category, Review, Ticket, Event, Gallery, BlogPost, Order
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

# User Registration View
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_active = True
        user.save()

        
# User List and Detail Views
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# Category Views
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Event Views
class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Ticket Views
class TicketListView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Gallery Views
class GalleryListView(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [AllowAny]

class GalleryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Review Views
class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# BlogPost Views
class BlogPostListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Order Views
class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
