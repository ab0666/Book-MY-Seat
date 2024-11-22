from django.db import models

from django.contrib.auth. models import User

import datetime
import os

# Create your models here.

def get_file_path(request, filename):
    original_filename = filename
    nowtime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowtime, original_filename)
    return os.path.join('uploads/', filename)

class Category(models.Model):
    slug = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    descriptions = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
    meta_title = models.CharField(max_length=50, null=False, blank=False)
    meta_keywords = models.CharField(max_length=50, null=False, blank=False)
    meta_descriptions = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    event_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    small_descriptions = models.CharField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    descriptions = models.TextField(max_length=500, null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
    tag = models.CharField(max_length=50, null=False, blank=False)
    meta_title = models.CharField(max_length=50, null=False, blank=False)
    meta_keywords = models.CharField(max_length=50, null=False, blank=False)
    meta_descriptions = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=5000, default="")

    def __str__(self):
        return self.name
    
class Queue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=False)
    phone = models.ImageField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_id = models.CharField(max_length=250, null=True)
    Bookingtatues = {
        ('Pending', 'Pending'),
        ('Confirmed and Processing', 'Confirmed and Processing'),
        ('Booking Confirmed', 'Booking Confirmed')
    }
    status = models.CharField(max_length=150, choices=Bookingtatues, default='In Progress')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} = {}'.format(self.id, self.tracking_no)
    
class BookingItem(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{} {}'.format(self.booking.id, self.booking.tracking_no)
