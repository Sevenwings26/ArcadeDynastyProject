## models 
# User
# Category
# Ticket
# Gallery
# Event
# TicketOrder
# Location
# Blog (optional)

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/')
    # video = models.FileField(upload_to='event_videos/', null=True, blank=True)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    TICKET_TYPES = [
        ('VIP', 'VIP'),
        ('General', 'General Admission'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50, choices=TICKET_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    payment_reference = models.CharField(max_length=100, null=True, blank=True)

class Gallery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=200, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    payment_reference = models.CharField(max_length=100, null=True, blank=True)
    tickets = models.ManyToManyField(Ticket)

