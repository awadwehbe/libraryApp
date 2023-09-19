from django.contrib import admin
from .models import Book
"""
In your Django app's admin.py file (create one if it doesn't exist), you need to register the Book model (or any other model you want to manage)
 with the admin interface. Here's an example of how to do it:
"""

admin.site.register(Book)
