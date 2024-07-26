from django.urls import path
from .views import ( 
    UserListView, UserDetailView, CategoryListView, CategoryDetailView,
    EventListView, EventDetailView, TicketListView, TicketDetailView,
    GalleryListView, GalleryDetailView, ReviewListView, ReviewDetailView,
    BlogPostListView, BlogPostDetailView, OrderListView, OrderDetailView,
    CreateUserView
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('galleries/', GalleryListView.as_view(), name='gallery-list'),
    path('galleries/<int:pk>/', GalleryDetailView.as_view(), name='gallery-detail'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('blogposts/', BlogPostListView.as_view(), name='blogpost-list'),
    path('blogposts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
